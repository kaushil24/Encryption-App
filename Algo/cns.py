class cns():


  def encpt(pt, key):
    pt+=' '
    pt = [ord(i) for i in pt]
    key = [ord(i) for i in key]
    cry = [i^key[0] for i in pt]
    for k in key[1:-1]:
      cry = [i^k for i in cry]

    cry = [i<<key[-1] for i in cry]
    op = ''
    for i in cry:
        op = op+str(i)+' '
        
    return op[:-1]

  def dcpt(cry_t, key_o):
    cry_t = cry_t.split(" ")[:-1]
    cry = [int(i) for i in cry_t]
    key_o = [ord(i) for i in key_o]
    key = [key_o[i] for i in range(len(key_o)-1, -1, -1)]
    cry = [i>>key[0] for i in cry]
    dcpt_t = [i^key[1] for i in cry]
    
    for k in key[2:]:
      dcpt_t = [i^k for i in dcpt_t]

    
    dcpt = [chr(i) for i in dcpt_t]
    pt = ''.join(dcpt)
    
    return pt
