import setup_script as ss
import playlist_logic as pl
import tracks_logic as tl

def main():
    pl.write_to_csv(ss.PATH)
    tl.write_to_csv(ss.PATH)

if __name__ == "__main__":
    main()