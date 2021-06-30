#-*-coding:utf-8-*-
def updata_init_data(self):
    new_init_data = self.sheet2.cell(2, 2).value
    self.sheet2.cell(2, 2).value = str(int(new_init_data) + 3)
    self.save_excel()
    print(new_init_data)