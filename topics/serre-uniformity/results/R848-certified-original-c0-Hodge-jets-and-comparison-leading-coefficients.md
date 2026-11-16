# R848：原 c0 六组 Hodge 一阶与五个比较首项的准确计算

日期：2026-11-16。会话：serre-public-astra-20261115。

**状态：本项实际完成。** 对原 p=41、原点 c0/P0、原粗参数 t=a³，
六个原 V_j=U_j/E6 的值和一阶、六个 W_h 及 λ_h³、真实七次相对
Norm/Trace，以及五个原比较函数的首项常数和一次系数均已准确生成。
特别地，五个一次系数 d_j 的原 s 坐标实际为零，有理坐标均非零。

实际公开 run [43790534424](https://github.com/Rogerhu12/math-research-public/actions/runs/43790534424)，
compute job **133047756159**，source
**a576ab9d3b6d155027ec6f52cb689205ee5e9b98**，
于 **2026-11-16T02:11:14.778784+00:00** 完成。
核心用时 **2.684693114 秒**，共 **24 个完成数学阶段**。
本项为具体主函数的原首项与纤维比较输入，不宣称原高度或 Serre 一致性已完成。

## 1. 五个实际首项

保留 [原 c0 纸证](../notes/2026-11-16-original-c0-Hom-nonramification-and-comparison-leading-terms.md)
的全部对象和规范。对五个 g_j=(1+T^j)f，写原比较函数为
\[
 \mathcal R_j
 =\frac{N_{L/K}(y_{g_j}^2-b)^{q_j}}
        {N_{L/K}(y_f^2-b)^{p_j}}.
\]
原 t=a³ 下，准确展开是
\[
 \mathcal R_j(t)=
 \kappa_j\,t^{14(p_j-q_j)}
 \bigl(1+d_jt+O(t^2)\bigr),\qquad \kappa_j\ne0.
 \tag{848.1}
\]

| j | 原 p_j | 原 q_j | 原 t 阶 | 实际 d_j |
|---:|---:|---:|---:|---|
| 1 | 165 | 67 | 1372 | $\dfrac{400661273054954455663176877995}{669684615259995069632138452}$ |
| 2 | 93 | 67 | 364 | $\dfrac{7547266135863789547828743}{69742206835819378839340}$ |
| 3 | 100 | 67 | 462 | $\dfrac{14467768307923106511728656587}{68310756108594155378050328}$ |
| 4 | 168 | 67 | 1414 | $\dfrac{525896852580586476231376905}{849313441290426908060344}$ |
| 5 | 371 | 134 | 3318 | $\dfrac{5001104587114811254609532703753}{3429738720280032072321473608}$ |

此处 d_j 是去掉首单项式后的单位幂级数的一次系数；
“单位幂级数”不表示 d_j 是原素数41处的单位。
表中数值直接读取准确 K 基 (1,s)、s²=−3 的两个坐标，第二坐标均为
(0,1)，没有先投影到有理部分。五个显示的有理数的分子、分母均为正，
所以特别给出 d_j≠0。

令
\[
 V_j=U_j/E_6,\quad W_0=V_0,\quad
 W_j=(V_0+V_j)^3/V_0^2\ (j=1,\ldots,5),
\]
\[
 M_h=N_{L/K}(108W_h(0)),\qquad
 T_h=\operatorname{Tr}_{L/K}\bigl(W_h'(0)/W_h(0)\bigr).
\]
准确常数仍为
\[
 \kappa_j=\frac{M_0^{\,2p_j}}{M_j^{\,2q_j}},
 \qquad d_j=\frac{p_jT_0-q_jT_j}{2}.
 \tag{848.2}
\]
每个 κ_j 已作为以两个实际原 Norm 为叶的五节点整数幂/除法 DAG 保存；
所有分母准确非零。没有展开巨大整数幂，没有取立方根或更换 CM 周期。

实际六个 M_h 的原1坐标均为零、s坐标均非零，即 M_h=s m_h，
其中 m_h∈Q×。因此由 s²=−3，在不展开幂的情况下有纸面恒等式
\[
 \kappa_j=(-3)^{p_j-q_j}
       \left(\frac{m_0^{p_j}}{m_j^{q_j}}\right)^2\in\mathbf Q^\times.
 \tag{848.3}
\]
五个差分别为98、26、33、101、237，所以在实数嵌入下 κ_j 的符号依次
为正、正、负、负、负。这里保留原真实 Norm 和相位；该符号不是由任择
平方根得到。

## 2. 准确计算的依据与范围

计算只消费已成来源：R803的原六组完整 M6 坐标（19件）、R837的原
P0 正则值（9件）、R791的原五方向及规范（7件），共35件。
未重新求 M6、Fourier、CM 值、原大矩阵、全局 A/B 或 Hom。

写 A_{j,r} 为**未缩放**的原 M6 坐标，Φ_i 为原
(82² T_i)E6/E4² 在 P0 的正则值。已证明的准确公式为
\[
 V_j(0)=A_{j,692}-\frac{A_{j,693}}{24s},
\]
\[
 V_j'(0)=
 -\frac4{82^2}\bigl(A_{j,690}\Phi_0+A_{j,691}\Phi_{73}\bigr)
 -\frac{A_{j,693}}{12s}.
 \tag{848.4}
\]
其余690个基向量在该局部除以E6后带 R²=O(t²)，故此阶不需其新
Taylor 计算，也不需 Φ 的导数。原82、1722及108规范全部保持不变。
原 Ramanujan 公式的公共因子一次项为零，给 λ_h³=108W_h(0)，以及
(848.2) 的准确常数和负号。

计算在原 L=Q(b,s) 的14维基中使用准确有理数运算，所有场逆和显示商
均乘回。相对 L/K 的七次 Norm 是原 K 乘法矩阵的行列式，Trace 是其
迹；每个行列式保留七步主元记录及逆乘回。它们不是在同一目标上取
七个 T 次幂的替代乘积，也没有丢弃原 b、ρ 或缩放常数。

24个完成阶段为：1个原来源审计、6个V一阶、6个W/λ³一阶、
6个真实Norm/Trace、5个比较首项。六个V值、六个W值及全部分母均
准确非零。数值完成不是由预填 d_j≠0 或假设 κ_j∈Q 得到；
这两项由实际输出和上述纸面推论给出。

## 3. 实际来源及输出身份

方法：[原 c0 Hodge jets 与首项消费契约](../notes/R803-original-c0-Hodge-jets-and-comparison-leading-coefficients-method.md)，
SHA **6a277f7933176ad24781294c05dcb570366d4a42d69b8c719439c69160bb87d8**。
纸证 SHA **d29ef204c77e7abe1b61ed50628574f58fc46f684ad4d00f8495ecd15c6a9073**。

入口：[公开请求](../notes/R803-c0-Hodge-jets-public-request.json)、
[准确核心](../scripts/R803_original_c0_Hodge_jets.py)、
[来源包装器](../scripts/R803_original_c0_Hodge_jets_public.py)。
工作流为 .github/workflows/serre-original-c0-Hodge-jets.yml，
全部新数学只在本公开仓库 Actions 执行。

| 项目 | 字节 | SHA-256 |
|---|---:|---|
| 准确核心 | 34699 | 4f8a41933c16727932308a52100376a86dc8b4e57458c4559ab00648fc33019e |
| 包装器 | 32414 | a7b91ecd18b8f185e4f1a78ef82549c0ce4d8f56fa62dde4f707f48550cbf7d2 |
| 最终数学证书 | 13827 | 775a07af76479e2b891caae410677a49265df34c0df02d979e74d33be663e09a |
| 来源审计 | 5778 | 39edf73cc9e809b3381eb5a99610129e689c78a19aa6225eab7970f546d60bf8 |
| 24阶段 manifest | 5074 | 5b597a39077c49173f1d6c854efd334122d542bc45b5ceea6d924f06ddbdc019 |
| 全输出 manifest（34项） | 5889 | b90422a5c839f59cfa500d717c83ab7b27352dbbac44d1d8beecd279f0b4d049 |
| 35件原输入 inventory | 8013 | 923791ad74ad350423922404cae87c402827780929b3992cf0f3fe955ddbd52e |
| 原输入载体 | 159207663 | 0eb191635beb51a1eb6d61d87624d74480d8d526b94efe7c22f282322d93a02c |

数学配置指纹为 **06d8d96e468abc71be779d34084cdbb17bbe40ea779e1f198e7f58366110c78f**；
35源身份指纹为 **d689a0392dd98b3e972fc368cce8692e14ced4388ab59e7abfadd73884185456**。
实际请求 SHA **f1107aa8df071c6296aaf24138b9ec0b3b061361d2b25504d34331b860f158cd**。

五个比较首项阶段的准确身份：

| j | 字节 | SHA-256 |
|---:|---:|---|
| 1 | 5035 | b5c5926b7ce275863fdb4390428e98f6dc3a1e37a4c30b3c2af476a0f4c64e81 |
| 2 | 5014 | bf6e4f9fbe9e4f2260e68550167961055965dd7349bc2e5d812ac6a899f017ba |
| 3 | 5028 | 2b58ed5b072ccde7f8026d4fd0f70b77b6907d477345656b23f6e418b0f22319 |
| 4 | 5022 | e314bc54f714b8feeda5ca40566b1c5af05302b6d45d9298551ec4ac95e7ccee |
| 5 | 5037 | c0bc4bd3c04a54fcb14c8117806a95d1512ff55742619a5aaacb2e7b6194ca60 |

文件名为 R803-c0-original-comparison-leading-jet-jN.json.gz，N为对应序号。
最终证书名为 p41-original-c0-Hodge-jets-and-comparison-leading-coefficients-certificate.json。

一日 artifact **14191923906**，名称
serre-global-R803-original-c0-Hodge-jets-and-comparison-leading-coefficients-43790534424-1，
ZIP **159795243B** / **1aa8c65d83443f56095bcda4abd7958f98f8d944cb83fbb984cd32aa9940b625**，
到期2026-11-17T02:11:15Z。根会话以11次Range读取33个小成员，共593816B，
逐项核原 manifest/SHA与父子配置；本次没有重新下载或声称重哈希整ZIP。
原35件大来源已由 producer准确绑定并随新载体保存。机器输出不进入Git或Release。

## 4. 对原后继的意义

原 c0 的局部比较不再缺 κ_j 或 d_j 的准确输入。
在原固定单项式帧下，三次线丛比较的纤维标量必须用这里的 κ_j；
单位幂级数一次修正必须用这里的 d_j。真实原 R_j(c1) 和对数一阶
可直接接 [R844](R844-certified-original-five-Hom-word-points-and-comparison-values.md)
与 [R847](R847-certified-original-five-comparison-logarithmic-jets-nonzero.md)。

本项未用 t 的幂改变全局比较函数，也不把 c0 的局部归一形式当成
c1 的原全局函数。原 Picard/Poincaré 线丛、theta二挠、规范有理截面、
非p高度项及实际 splitting 仍须以原对象继续处理。
五个 d_j 非零不是高度非零、A.1接受或全p证明。
