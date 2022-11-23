from src.ConsoleMasterPy import ConsoleMaster, generate_name

cm = ConsoleMaster()

while 1:
    cm.clean_windows()
    print(generate_name())
    cm.pause()
