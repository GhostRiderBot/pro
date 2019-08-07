        if op.param1 in wait['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if op.param2 in wait['ROM'][op.param1]:
               pass
            else:
                if op.param1 in wait["cyduk"]:
                  if " " in Name:
                    nick = Name.split(' ')
                    if len(nick) == 2:
                       try:
                          if '~' in wait["ctc1"]:
                             sendtag(op.param1, wait["ctc1"] ,[op.param2])
                          else:
                             sendtag(op.param1, 'Loh ada ~    \n' + wait["ctc1"] ,[op.param2])
                       except Exception as e:
                           print(e)
                    else:
                        try:
                          if '~' in wait["ctc2"]:
                             sendtag(op.param1, wait["ctc2"] ,[op.param2])
                          else:
                             sendtag(op.param1, 'Halo ~    \n' + wait["ctc2"] ,[op.param2])
                        except Exception as e:
                            print(e)
                  else:
                    try:
                        if '~' in wait["ctc3"]:
                             sendtag(op.param1, wait["ctc3"] ,[op.param2])
                        else:
                             sendtag(op.param1, 'Hayoo ngintip si ~    \n' + wait["ctc3"] ,[op.param2])
                    except Exception as e:
                        print(e)
                else:pass

def sendtagdef sendtag(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@mbahdon "
    if mids == []:
        raise Exception("Invalid mids")
    if "~" in text:
        if text.count("~") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("~")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)