# R150：一般 W 的四条 S-free 原三次式、原理想相等与二元三次头结式

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。

## 1. 精确输入与结论

沿用已刊“三条原 S 一次式及两个几何变量的完整二次系统降维”的同一个原系统与局部环。其实际源 SHA256 为
`4da946c486a2e3ca9b22faa16df13f8e24068ea390eed52135a1f2e49dcd6a30`，
成功 run 45967269487 / job 140398862236，正式提交
`8c7f1580abcd7df252ea4f8b8f1306ba4b526dfb`。
物理坐标仍是 $F=2f-u\lambda,S=T-2\lambda$。

此前已经得到
$$
q_0=S^2+LS+C,
$$
$$
Q_F=\delta FS+B_F,\quad
Q_\lambda=\delta\lambda S+B_\lambda,\quad
Q_*=\delta S+B_*,
$$
其中 L 至多一次，C 与三个 B 至多二次，均只含 $F,\lambda$；$\delta$ 只含权参数，唯一未付非单位因子为 $D_{27}$。这些均保存对同一个完整原六式的实际迹。

三条原 S-free 必要式是
$$
G_F=FB_*-B_F,\quad
G_\lambda=\lambda B_*-B_\lambda,\quad
G_4=B_*^2-\delta L B_*+\delta^2C. \tag{1}
$$
本附录将其原理想准确改写为四个总几何次数至多 3 的原多项式。没有除 $\delta$、任何几何变量或新的头系数；$D_{27}=0$ 面仍保留。

## 2. 完整四三次恒等式与双向原理想相等

将 $B_*$ 按几何次数分开：
$$
B_*=q_2+h_1+c_0,\qquad
q_2=aF^2+bF\lambda+c\lambda^2.
$$
令
$$
Z=aF+b\lambda,\qquad Y=c\lambda,
\qquad ZF+Y\lambda=q_2. \tag{2}
$$
这里 a、b、c 是该二次头的参数系数，不是原 Gram 权。即使其中任何系数为零，(2) 仍成立。

第一条新增原式是
$$
G_\times=\lambda G_F-FG_\lambda
=FB_\lambda-\lambda B_F. \tag{3}
$$
右端次数不超过 3；两个四次项已经准确抵消。

第二条新增原式为
$$
\begin{aligned}
G_{\rm red}
&=G_4-ZG_F-YG_\lambda\\
&=B_*(h_1+c_0-\delta L)+\delta^2C+ZB_F+YB_\lambda.
\end{aligned} \tag{4}
$$
第二行每项次数至多 3。等式直接由 (1)、(2) 展开；尤其没有用 $q_2$ 的任一系数作分母。

式 (3)、(4) 连同反向身份
$$
G_4=G_{\rm red}+ZG_F+YG_\lambda \tag{5}
$$
证明，在整个已付局部环的 $F,\lambda$ 多项式环内，
$$
(G_F,G_\lambda,G_4)
=(G_F,G_\lambda,G_\times,G_{\rm red}). \tag{6}
$$
这是原理想相等，不只是零集相等。若原三条迹为 $\tau_F,\tau_\lambda,\tau_4$，新两条迹明确为
$$
\lambda\tau_F-F\tau_\lambda,\qquad
\tau_4-Z\tau_F-Y\tau_\lambda;
$$
所以原理想来源同时完整保留。对各行另作已付单位归一化不会改变 (6)。

在 $D_{27}\ne0$ 图，结合此前已证明的 $S=-B_*/\delta$ 双向恢复，四条三次式准确替代原四二次系统。在 $D_{27}=0$ 图，本附录仍只提供原必要式及 (6) 的 S-free 理想相等，必须保留原 $q_0,Q_F,Q_\lambda,Q_*$；不利用 (6) 擅自解 S。

## 3. 二元三次头的完整通用矩阵

设三个 B 的二次头分别是
$$
q_2=aF^2+bF\lambda+c\lambda^2,
$$
$$
q_F=dF^2+e_0F\lambda+f\lambda^2,\qquad
q_\lambda=gF^2+hF\lambda+i\lambda^2.
$$
此处九个字母只是彼此独立的通用系数；$e_0$ 不与权参数 e 混同。

$G_F,G_\lambda,G_\times$ 的三次头分别为
$$
Fq_2,\qquad\lambda q_2,\qquad
g_3:=Fq_\lambda-\lambda q_F.
$$
$G_{\rm red}$ 的三次头为
$$
q_2(h_1-\delta L)^h+Zq_F+Yq_\lambda.
$$
第一项只是前两条三次头的参数线性组合。因此减去该组合后，按列 $(F^3,F^2\lambda,F\lambda^2,\lambda^3)$，头矩阵成为
$$
\mathcal H=
\begin{pmatrix}
a&b&c&0\\
0&a&b&c\\
g&h-d&i-e_0&-f\\
ad&ae_0+bd+cg&af+be_0+ch&bf+ci
\end{pmatrix}. \tag{7}
$$
该行变换不使用除法。对已付单位归一化后的四条实际原式，头行列式只额外乘一个已付单位，零面与 (7) 一致。

## 4. 不丢首项零的通用结式身份

有完整的整数多项式恒等式
$$
\det\mathcal H
=\operatorname{Res}_{\rm bin}(q_2,g_3), \tag{8}
$$
右端按固定二次、三次齐次次数定义。其固定 Sylvester 矩阵为
$$
\begin{pmatrix}
a&b&c&0&0\\
0&a&b&c&0\\
0&0&a&b&c\\
g&h-d&i-e_0&-f&0\\
0&g&h-d&i-e_0&-f
\end{pmatrix}. \tag{9}
$$
因此 (8) 保留 $a=0$、$c=0$、二次头退化、三次头退化及重复根；没有先除首项或用单个仿射图替代齐次结式。

两边直接行列式展开得到同一个 26 项五次通用多项式：
$$
\begin{aligned}
&c^3g^2-bc^2gh+bc^2dg+b^2cgi-b^2ce_0g+b^3fg\\
&+ac^2h^2-2ac^2gi+2ac^2e_0g-2ac^2dh+ac^2d^2\\
&-abchi-3abcfg+abce_0h+abcdi-abcde_0-ab^2fh+ab^2df\\
&+a^2ci^2+2a^2cfh-2a^2ce_0i+a^2ce_0^2-2a^2cdf\\
&+a^2bfi-a^2be_0f+a^3f^2.
\end{aligned} \tag{10}
$$
本会话用九个独立形式变量的 BigInt 整系数稀疏多项式，实际分别展开 (7)、(9) 并检查差为零；没有数值取样或特征 p 输入。式 (10) 也保留了全部共同系数，故这一通用身份可直接逐项审查。

若将来某个明确权子图中 (8) 是真单位，实际余子式逆将给出全部四个二元三次单项式的首一原规则，从而由
$$
1,F,\lambda,F^2,F\lambda,\lambda^2
$$
生成该 S-free 商。这里没有声称 (8) 目前已全图支付；它的零面与 $D_{27}=0$ 都保留。原 $N_s/P_s$ 仍须在同一个恢复的 S 上返回，(6) 不代替这些剩余原约束。

## 5. 实际通用证书及新的原权头输入

通用整数恒等式源为一个可由 JavaScript Function 调用的自含函数体：
`notes/2026-11-27-unit211-W-four-cubic-universal-head-resultant-8542.js`。
使用 `new Function(sourceText)()` 再生返回对象。

Git blob `08bc6c6f9f878a3d0a444bbc75cb6ac235257afc`，
2152 字节，SHA256：
`089f0d5d5dc1f3ed5333b5642f210b943fee1e7fa80cc18899bc749e53ff8098`。

实际 functions.exec V8 执行耗时 1 毫秒，26 项全部相同，总系数次数 5，没有倒置任何系数。OS 退出码不适用，RSS 未暴露。完整返回对象 1233 字节，Git blob
`ac4e1901ee14871cdcff0d62c48258d6fe909fd2`，SHA256：
`5f73cd77c5c9fb44e9917efa069ae1091d27ae30457824e3e4587edbbba19583`。

另已构造一次新的 W 原权输入：
`notes/2026-11-27-unit211-generic-LS-W-four-S-free-original-cubics-and-binary-head-8542.py`，
Git blob `d015fb9c74d80e01ee648edd819b11838659bc12`，
18167 字节，SHA256：
`00c08b48852bc8c38041a617d616922c94b6ab0e6f66c393a7e679949b44568e`。
它以此前原 S 一次系统为必要前缀，逐项核 (3)–(5) 的完整原迹，实际形成四条归一化三次式及固定四列头，精确分解头行列式并保所有未付因子；边界 180 秒、4 GiB。**该 Python 输入在本稿形成时尚未执行**，不能把通用九系数证书冒充其已实际成功，也不预报它在 W 参数上的因式。

本附录没有运行旧参数 cofactor 或旧 Gröbner 门。它完成的是新的原理想降次与不丢首项的通用头公式；整个 W 有限系统和普通 ISP 尚未由此排空。

