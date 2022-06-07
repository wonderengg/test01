import re
long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

result = {};

pro_text = long_text.split('\n');

sub_fund = [];
sub_fund_dic = {};
isin = [];

result["name"] = pro_text[1];
result["lei"] = pro_text[2];

for i in range(3, len(pro_text)):
    # title里有.，根据此来判断该元素是否属于title
    if (pro_text[i].find('.') != -1):
        pro_text[i] = re.sub(r'[0-9]+','',pro_text[i])
        pro_text[i] = re.sub(r'\.', '', pro_text[i])
        # 用于对sub_fund里不同的字典进行划分
        if (len(isin) != 0):
            sub_fund_dic["isin"] = isin;  # 完成一个isin列表
            sub_fund.append(sub_fund_dic);  # 完成一个字典块
            #初始化为下个sub_fund里的字典做准备
            sub_fund_dic = {};
            isin = [];

        # 命名标题
        sub_fund_dic["title"] = pro_text[i];
    else:
        isin.append(pro_text[i]);

if (len(isin) != 0):
    sub_fund_dic["isin"] = isin;
    sub_fund.append(sub_fund_dic);

    sub_fund_dic = {};
    isin = [];

result["sub_fund"] = sub_fund;
print(result);