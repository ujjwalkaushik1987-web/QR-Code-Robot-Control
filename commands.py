def map_command(data):
    data = data.strip().upper()

    if data == "START":
        return "SayEZB('Started')"
    elif data == "LEFT":
        return "ControlCommand(\"Movement Panel\", \"Left\")"
    elif data == "RIGHT":
        return "ControlCommand(\"Movement Panel\", \"Right\")"
    elif data == "STOP":
        return "ControlCommand(\"Movement Panel\", \"Stop\")"
    return ""
