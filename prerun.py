from docx import Document
from styles import Styles, Decider
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    old_document = Document("input/" + args.file)

    styles = Styles(old_document)
    custom_style_names = True
    if custom_style_names:
        Decider.custom_names(styles)

    old_document.save('input/work_c.docx')


if __name__ == "__main__":
    main()
    print("!")
