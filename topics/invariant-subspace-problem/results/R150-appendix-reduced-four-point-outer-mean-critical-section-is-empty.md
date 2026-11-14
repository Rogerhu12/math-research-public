# R150 附录：四个不同支点的外均值完整临界截面为空

日期：2026-11-14（UTC）。作者：normal_resume_2220 / Astra-ISP-1cf8c51d。

状态：**已证明。** 对原六模模型，若均值 catalecticant 秩为三、第三普通矩的本质空间 \(W\) 为三维、\(y\notin W\)，且唯一长度四支撑由四个不同物理点组成，则不存在原完整临界点。本稿完成此前剩余的唯一 \(2+2\) 半权分割。论证保留所有允许的复权、零单个偏度参数以及投影中心相切的原分支；已单独排除的分母零支不被默默删除。

## 1. 已支付的分支与当前原数据

[全部外均值降秩排除](R150-appendix-no-secant-cuspidal-companion-and-outer-mean-rank-drop-exclusion.md)已证明 \(H\) 必秩四；[四不同有基点排除](R150-appendix-reduced-four-point-basepoint-critical-section-is-empty.md)已证明四维物理五次映射无基点。沿用同一原中心泛函 \(\lambda\) 将四个物理代表归一为
\[
\lambda(u_i)=1,\quad
y=\sum_iw_i u_i,\quad H=\tfrac14\sum_iw_i u_i^2,\quad
V=\tfrac18\sum_iw_i u_i^3,\quad w_i\ne0.
\]
[单点半权排除](R150-appendix-reduced-four-point-single-half-weight-exclusion.md)后，唯一的半权分割可以编号为
\[
w_0+w_1=w_2+w_3=\tfrac12.
\]
原中央三次是不可约普通节点三次，原物理参数化是其归一化。

沿用[相等半块配对排除](R150-appendix-reduced-four-point-equal-half-block-pairing-exclusion.md)的正交基：
\[
\mathcal M=H-\tfrac14y^2=\tfrac14I_W,\qquad
C=T_3=\tfrac32U(L^2-M^2)+rL^3+sM^3,
\]
\[
K_W=\begin{pmatrix}f&d&e\\d&a&c\\e&c&b\end{pmatrix},\quad
p=(Ky)|_W=((b-a)/2,-d-ra,e-sb),\quad
2F=-\operatorname{tr}K_W.
\tag{1.1}
\]
物理四点分别是 \(y+U+\eta L\)、\(y-U+\zeta M\)，其中
\[
\eta^2-2r\eta-2=0,\qquad \zeta^2-2s\zeta-2=0.
\tag{1.2}
\]
唯一半权分割给
\[
r^2+2\ne0,\quad s^2+2\ne0,\quad r^2\ne s^2.
\tag{1.3}
\]
其中 \(r=0\) 或 \(s=0\) 都允许。

设 \(h=(a+b)/2,\ \Delta=(a-b)/2,\ Z=(c^2-h^2)/2\)。下列原整支已经单独排除：

- [某半块内部配对为零](R150-appendix-reduced-four-point-half-block-pairings-are-nonzero.md)；
- [两半块配对相等，即中心相切](R150-appendix-reduced-four-point-equal-half-block-pairing-exclusion.md)；
- [\(Z=0\)](R150-appendix-reduced-four-point-zero-Z-branch-exclusion.md)；
- [\(h=0\)](R150-appendix-reduced-four-point-zero-h-branch-exclusion.md)。

因此当前必有
\[
h\Delta abZ\ne0.
\tag{1.4}
\]
所有必要梯度方程在 Gram 配对中齐次。整体除以 \(h\)，记 \(\delta=\Delta/h\)，可以取
\[
h=1,\quad a=1+\delta,\quad b=1-\delta,\quad
\delta\ne0,\quad\delta^2\ne1,\quad c^2\ne1.
\tag{1.5}
\]
这只是齐次方程的代数归一，不另选原物理核。

## 2. 完整均值方程的无遗漏参数化

此前已从原完整均值向量证明四个精确二次方程
\[
a(f+r^2a+2rd)=Z,\quad b(f+s^2b-2se)=Z,
\]
\[
hd-ce=r(Z-h\Delta),\quad cd-he=s(Z+h\Delta).
\tag{2.1}
\]
因 \(Z\ne0\)，后两式唯一决定 \(d,e\)，再因 \(a\ne0\)，第一式唯一决定 \(f\)。两种 \(f\) 的相容性在 \(\Delta\ne0\) 下给
\[
ab\big[(r^2+s^2)(c^2+h^2)+4hcrs\big]+(c^2-h^2)^2=0.
\tag{2.2}
\]

定义
\[
X=\frac{r+s}{c-1},\qquad Y=\frac{r-s}{c+1}.
\]
由 (1.3)、(1.5)，\(X,Y\ne0\)。反解为
\[
r=\tfrac12((c-1)X+(c+1)Y),\quad
s=\tfrac12((c-1)X-(c+1)Y).
\tag{2.3}
\]
相容式 (2.2) 正好变成
\[
(1-\delta^2)(X^2+Y^2)+2=0.
\tag{2.4}
\]
把下面的 \(d,e,f\) 代回 (2.1)，余式都是 (2.4) 的倍数：
\[
4d=(c-1)^2X-(c+1)^2Y+2\delta(X-Y),
\]
\[
4e=-(c-1)^2X-(c+1)^2Y+2\delta(X+Y),
\]
\[
4f=-(c^2+1)\big[(c-1)X^2-(c+1)Y^2+2\delta XY\big].
\tag{2.5}
\]
结合上述唯一性，这些就是每个原剩余候选的实际 Gram 数据；没有只构造一个充分子族而漏掉其余解。

附属脚本用整数多项式分别验证 (2.5) 的四个均值方程身份。整个参数化没有除以 \(r,s,c\)。

## 3. 原最高、二阶梯度的准确代数输入

对于极线坐标 \((\rho,q)\in\mathbb C y^*\oplus W^*\)，使用同一原二阶梯度：
\[
4N(\rho,q)=2\rho\,p\cdot q+4C(p,q,q)
 +2F\,q\cdot q+q^{\mathsf T}K_Wq.
\tag{3.1}
\]
把 (1.2) 的四个实际物理代表代入，分别对两条二次方程取余。记最高式的常数、一次余式为 \(C_{+0},C_{+1},C_{-0},C_{-1}\)，二阶式对应为 \(H_{+0},H_{+1},H_{-0},H_{-1}\)。它们都是原完整梯度的必要条件。

为固定下面证书的整数归一，脚本先计算 \(16C(q)\)、\(16N(\rho,q)\) 的余式，代入 (2.3)—(2.5)，清除固定的二次幂整数分母，然后按
\[
\delta^2X^2=-\delta^2Y^2+X^2+Y^2+2
\tag{3.2}
\]
约化，最后除去每个多项式的正整数内容。这个步骤只使用 (2.4)，不作新的非零假设。以下 \(C_{\pm j},H_{\pm j}\) 均指这组确定的整数归一。

令
\[
\mathsf U=X^2+Y^2,\quad \mathsf V=X^2-Y^2,\quad \mathsf W=XY,\quad z=c^2-1.
\]
于是
\[
\mathsf U=\frac2{\delta^2-1},\qquad
\mathsf V^2+4\mathsf W^2=\mathsf U^2,\qquad \mathsf W\ne0.
\tag{3.3}
\]
原常数余式之差给出以下两个必要方程：
\[
S_1=-z(\mathsf U+c\mathsf V)+4\delta^3\mathsf W=0,
\tag{3.4}
\]
\[
S_2=\delta\!\left[-\mathsf U z(c^2+1)
 +2c(z-2\delta^2)\mathsf V+8(\delta^2-z)\right]
 -2z(z-2\delta^2)\mathsf W=0.
\tag{3.5}
\]
准确身份为
\[
(H_{+0}-C_{+0})+(H_{-0}-C_{-0})=16zS_1,
\]
\[
(H_{+0}-C_{+0})-(H_{-0}-C_{-0})=8S_2
\]
模 (2.4) 成立。因 \(z\ne0\)，确实可推出 (3.4)—(3.5)。附属脚本逐项验证这两式。

## 4. 一个不除以 c 的一元参数

消去 (3.4)、(3.5) 中的 \(c\mathsf V\)，并使用 (3.3)，得到
\[
(\delta^2-1)(z-2\delta^2)^2(z+2\delta^2)\mathsf W
 +\delta z(z^2+4z\delta^2-4\delta^4)=0.
\tag{4.1}
\]
脚本核验的多项式身份为：\((\delta^2-1)[zS_2+2\delta(z-2\delta^2)S_1]\) 加上 (4.1) 左端的两倍，模 (2.4) 恒为零。

设
\[
t=\frac z{\delta^2},\quad x=\delta^2,\quad
\mathcal A(t)=t^2+4t-4,\quad
\mathcal B(t)=(t-2)^2(t+2).
\]
这里 \(\delta,z\ne0\)，所以 \(t\ne0\)。(4.1) 化为
\[
(x-1)\mathcal B(t)\mathsf W+\delta t\mathcal A(t)=0.
\tag{4.2}
\]
若 \(t=2\) 或 \(t=-2\)，第二项都等于 \(16\delta\ne0\)，矛盾。因此
\[
t\ne0,\quad t\ne2,\quad t\ne-2.
\tag{4.3}
\]
现在可以合法写
\[
\mathsf U=\frac2{x-1},\qquad
\mathsf W=-\frac{\delta t\mathcal A(t)}{(x-1)\mathcal B(t)},
\]
\[
c\mathsf V=\frac{4\delta\mathsf W}{t}-\mathsf U,\qquad
\mathsf V^2=\mathsf U^2-4\mathsf W^2.
\tag{4.4}
\]
没有一步除以 \(c\)，所以 \(c=0\) 的可能性仍完整保留。

## 5. 三条线性于 x 的整数必要方程

使用下面四个原剩余方程：
\[
C_{+0},\quad C_{-0},\quad
2r(C_{+1}-3H_{+1}),\quad
2s(C_{-1}-3H_{-1}).
\tag{5.1}
\]
它们在 \((c,X,Y)\mapsto(-c,Y,X)\) 下模 (2.4) 不变；脚本精确核验全部四个对称身份。对每个多项式与其对称像相加后，依次用

1. \(X^2=(\mathsf U+\mathsf V)/2,\ Y^2=(\mathsf U-\mathsf V)/2,\ XY=\mathsf W\)；
2. \(\mathsf V^2=\mathsf U^2-4\mathsf W^2\)；
3. \(c^2=1+\delta^2t\) 及 (4.4) 中的 \(c\mathsf V\)；
4. (4.4) 的 \(\mathsf U,\mathsf W\)；

进行代入。对称性保证线性于 \(\mathsf V\) 的项含一个 \(c\) 因子，因此仍无需除以 \(c\)。

清除 \((x-1)^2\mathcal B(t)^2\) 以及固定整数分母，除去已知非零的 \(\delta^5t\) 及正整数内容，得到四个整数多项式 \(\Phi_1,\ldots,\Phi_4\)，它们都必须为零。确定的组合是
\[
\Phi_1+\Phi_2=2\delta(A_0+xB_0),\quad
\Phi_3+\Phi_4=2\delta(A_1+xB_1),\quad
\Phi_3-\Phi_4=2(A_2+xB_2).
\tag{5.2}
\]
由于 \(\delta\ne0\)，原候选必须满足
\[
A_i(t)+xB_i(t)=0,\qquad i=0,1,2.
\tag{5.3}
\]

以下系数表完整给出这六个多项式，**数组按常数项到最高次项排列**：

    A0 = [-1536,1280,-896,-448,1056,80,-264,-68,20,-2]
    B0 = [0,-1536,1664,320,-32,240,-296,-116,-14,-1]

    A1 = [0,384,-1024,320,688,-328,-136,48,19,-4]
    B1 = [0,-384,704,-384,-32,296,-148,-20,24,4]

    A2 = [-1024,896,384,-288,64,72,-8,-14,4]
    B2 = [512,-1152,192,352,144,104,-76,-14,5]

附属自含脚本从原 (1.1)、(3.1) 开始重做所有代入，再逐系数比较此表；不是把系数表作为未经验证的输入直接断言结论。清分母只用到了 (1.4)、(1.5)、(4.3)，且容许 \(r=0\) 或 \(s=0\)。

## 6. 短一元矛盾证书

令 \(P,Q\) 分别是
\[
A_0B_1-B_0A_1,\qquad A_0B_2-B_0A_2
\]
的正首项本原部分。它们的次数分别为 \(18,17\)。精确整数伪余式算法给出
\[
\gcd_{\mathbb Q[t]}(P,Q)=(t+2)^2.
\tag{6.1}
\]
每次伪余除都只做整数乘减并除去整数内容；附件回执记录了全部余式次数链。

也可用以下小证书直接检查 (6.1) 中除去公共因子后的互素性。准确整除
\[
P=(t+2)^2P_*,\qquad Q=(t+2)^2Q_*
\]
后，两个商的升幂系数为

    P* = [0,-147456,393216,-262144,-129024,196608,-75264,68864,
          -1280,-81728,42688,5600,-7032,1304,26,-43,12]
    Q* = [98304,-204800,73728,-14336,31744,74752,-23808,-34304,
          -16896,21216,2240,-3992,-244,480,-97,3]

模 \(103\) 时，它们仍分别为 \(16,15\) 次，首项为 \(12,3\)。以下两个升幂数组给出显式 Bezout 身份 \(UP_*+VQ_*=1\pmod {103}\)：

    U = [66,11,31,91,26,93,63,96,59,72,43,42,8,92,74]
    V = [27,78,75,42,54,20,80,80,20,98,47,53,21,13,83,13]

因此商的整数 Sylvester 行列式模 \(103\) 非零（直接计算为 \(52\)），所以其在零特征中也非零，商在 \(\mathbb C\) 上无共同根。这里是完整次数下的整数行列式证书，不是将有限域点枚举当作复代数结论。

原方程 (5.3) 迫 \(P(t)=Q(t)=0\)，所以 (6.1) 迫 \(t=-2\)。这与已经由原常数梯度排除的 (4.3) 矛盾。

## 7. 原四不同截面全部关闭

当前 \(h\Delta abZ\ne0\) 分支已经排除。所有此前清除的分母零支均有独立完整证明，故没有剩余四不同支点候选。连同既有的原降秩、有基点、单点半权排除，得到本稿开头的整类结论：

> 原非割线均值、第三普通矩本质维数三、外均值且四个物理支点互异的完整临界截面为空。

本稿不把有限维临界分类扩张为自然匹配幂、原算子逆或普通复 Hilbert 不变子空间问题的解答。下一项工作继续处理 open.md 中尚未关闭的其它均值秩及本质维数截面。
