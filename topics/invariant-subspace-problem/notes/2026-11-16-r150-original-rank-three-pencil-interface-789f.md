# 原 rank3 例外、完整六次 pencil 与全部高亏秩门

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。2026-11-16。

~~~sh
python 2026-11-16-r150-original-mean-rank-three-exact-pencil-789f.py \
  --six-out SIX_OUT --out PENCIL_OUT --seconds 180 --memory-mib 768

python 2026-11-16-r150-original-pencil-complete-minor-coefficient-gates-v2-789f.py \
  --pencil-out PENCIL_OUT --out MINOR_OUT --seconds 90 --memory-mib 768

python 2026-11-16-r150-original-sextic-pencil-rabin-certificate-789f.py \
  --minor-out MINOR_OUT --out RABIN_OUT
~~~

三个源、原输入、所有实际中间 pins 见 inputs。第三源只依标准Python；
前两源使用 python-flint 0.9.0。所有输出仅留临时目录，执行身份只记录参数/源/run/输出SHA。

## 原参数运输

从同一原四张对称 $T_i$ 按21个上三角坐标取4列，固定127/d100只选常数单位行。
实际选中 $(0,0),(0,1),(0,2),(0,3)$。设该4×4原 $E$ 方块为 $U$、逆为 $V$。
规范张量 $T'_j=\sum_i T_iV_{ij}$，参数准确为
$$
\lambda=V\mu,\qquad\mu=U\lambda.
$$
32个双向常逆和全部84个原上三角坐标返回均实际精确核验。
不对 $\mu,y,w,u$ 特化；没有参数逆。

完整六次 $\Delta(\mu)=\det\sum_j\mu_jT'_j$ 用所有置换项的子集动态程序计算，
并保存全部84个真 $E$ 系数。7个域点只作为符号/顺序的独立检查，不替代完整精确计算。

## 系数单位门与实际完整范围

第二阶段从原规范张量及全部84个六次系数严格约127，保完整全部225个4阶minor，
以及全部21个对称5阶cofactor，未只检查某个参数点。

- 225个4阶minor的35行齐次系数满秩。所选35原列单位det=81，
  全2450个左右乘回通过。这在原 $E$ 中给 $I_4(T')=(\mu)^4$。
- 21个cofactor限制 $\mu_0=0$ 的21×21完整系数块det=103，
  全882个乘回通过。这给所有高亏秩参数位于 $\mu_0\ne0$；
  取 $\mu_0=1$ 后21个五次首项能消去全部三变量degree5单项式。
  因而完整corank2坐标代数至多35元生成；没有声称自由35或35个不同点。

每个域单位提升只倒固定 $E$ 常数系数方块。原cofactor/minor标签和全部系数都保留。
第一版仅在封存时遇 fmpz exponent JSON序列化错误，0.597583061秒/exit1；
v2明确把这些整数转成Python int。失败回执和源身份单独保留。

## 独立不可约证书

第二阶段的原六次域因式分解为一个6次因子，乘回全真；
第三阶段给不依赖该因式分解器的完整Rabin证书。
实际直线 $(\mu_0,\mu_1,\mu_2,\mu_3)=(1,0,7,x)$，
首项40、首一多项式
$$
x^6+45x^5+92x^4+116x^3+111x^2+57x+126.
$$
两条Bezout恒等式、完整六次Frobenius链、最后 $x^{127^6}=x\bmod f$ 均保存并实际核验。
$\mu_3^6$ 的原域系数40非零，所以该直线保持任何非平凡齐次因子的正次数；
这给完整原六次域多项式不可约，再由合法127系数place的Gauss引理提升到 $E$。
不声明绝对不可约。

## 必须保留的原例外

对 $y\ne0$，已付 $I_3(M)=(y)^3$。因此rank3恰由唯一 $[\mu]$ 的
$$
T'(\mu)y=0
$$
给出。所有六行必须保留。六次面上rank5的点有一条核线；
有限corank2参数处有完整二维核、投影核为整条 $\mathbb P^1$，不能删掉。
仅在真5阶单位开集才可用adj的一列代表 $y$。

这只是完整描述原rank3参数例外。原rank4支路、全部 $w,u$ 及9×56临界关系列仍需处理。
项目化的 $[y]$ 也不能替代原 Bell=1 模型中的非零尺度。
