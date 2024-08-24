import os
import sys
from hacking import fatal

FILENAME = "/var/notes"

def print_notes(fd, uid, searchstring):
    """Print the notes for a given UID that match an optional search string."""
    while True:
        note_length = find_user_note(fd, uid)
        if note_length == -1:  # End of file
            return 0
        note_buffer = os.read(fd, note_length).decode('utf-8')
        if search_note(note_buffer, searchstring):
            print(note_buffer)
    return 1

def find_user_note(fd, user_uid):
    """Find the next note for a given user ID."""
    while True:
        note_uid_bytes = os.read(fd, 4)
        if len(note_uid_bytes) < 4:
            return -1  # End of file
        note_uid = int.from_bytes(note_uid_bytes, 'little')
        if note_uid == user_uid:
            length = 0
            while True:
                byte = os.read(fd, 1)
                if len(byte) < 1 or byte == b'\n':
                    break
                length += 1
            os.lseek(fd, -length - 1, os.SEEK_CUR)
            print(f"[DEBUG] found a {length} byte note for user id {note_uid}")
            return length
        else:
            while True:
                byte = os.read(fd, 1)
                if len(byte) < 1 or byte == b'\n':
                    break

def search_note(note, keyword):
    """Search a note for a given keyword."""
    if not keyword:  # If there is no search string, always match
        return 1
    return 1 if keyword in note else 0

def main():
    if len(sys.argv) > 1:
        searchstring = sys.argv[1]
    else:
        searchstring = ""

    userid = os.getuid()
    try:
        fd = os.open(FILENAME, os.O_RDONLY)
    except OSError:
        fatal("in main() while opening file for reading")

    printing = print_notes(fd, userid, searchstring)
    print("-------[ end of note data ]-------")
    os.close(fd)

if __name__ == "__main__":
    main()
