import datetime,random,os

error_code = 0xffffff

error_grid = {
    0x000001:"密钥自动生成错误",
    0x000002:"密钥格式错误",
    0x000003:"未能正确识别明/密文",
    0x000004:"字符加/解密错误",
    0xffffff:"未知错误"
}

class enc_dec():
    def __init__(self):
        self.seed = None
        self.text = None
        self.enc = "1"
        self.dec = "2"
    def mainc(self,stat,text,seed):
        global error_code
        self.seed = seed
        self.text = text
        # self.seed = self.AutoSummonSeed()
        if stat == "1":    #1为加密
            if self.seed == None:
                self.seed = self.AutoSummonSeed()
            else:
                error_code = 0x000002
                self.seed = int(self.seed)
            self.public_text = text
            for i in self.public_text:
                if ord(i) < 42:
                    self.seed = abs(self.seed)
                    break
            return self.Encryption()
        elif stat == "2":    #2为解密
            self.seed = seed
            error_code = 0x000002
            self.seed = int(self.seed)
            self.private_text = text
            return self.Decrypt()

    def AutoSummonSeed(self) -> int:
        global error_code
        error_code = 0x000001
        src = ["%Y","%m","%d","%H","%M","%S"]
        random.shuffle(src)
        src = "".join(src)
        return int(datetime.datetime.now().strftime(src)[::-1])**2*(random.choice([1,-1]))//int(datetime.datetime.now().second)
    
    def Encryption(self) -> str:
        try:
            global error_code
            error_code = 0x000003
            of0 = (self.seed<0)
            seedpass = list(map(int,list(str(abs(self.seed)))))
            seed_lenth = len(seedpass)
            self.private_text = ""
            i = 0
            for s in self.public_text:
                error_code = 0x000004
                if of0:
                    self.private_text += chr(ord(s)-seedpass[i%seed_lenth])
                else:
                    self.private_text += chr(ord(s)+seedpass[i%seed_lenth])
                i += 1
            self.private_text = self.private_text[::-1]
            return self.private_text
        except:
            return "error"
    
    def Decrypt(self) -> str:
        try:
            global error_code
            error_code = 0x000003
            of0 = (self.seed<0)
            seedpass = list(map(int,list(str(abs(self.seed)))))
            seed_lenth = len(seedpass)
            self.public_text = ""
            self.private_text = self.private_text[::-1]
            i = 0
            for s in self.private_text:
                error_code = 0x000004
                if of0:
                    self.public_text += chr(ord(s)+seedpass[i%seed_lenth])
                else:
                    self.public_text += chr(ord(s)-seedpass[i%seed_lenth])
                i += 1
            return self.public_text
        except:
            return "error"