# R443 — 原残余四挠第二态的完整张量与真实中央返回

日期：2026-11-14。**状态：已证明。** R439 的真实第二残余态乘回原
独立 sigma 后，
$$
\mathcal K_1(w,q)=\sigma(26q)\mathcal L_1(w,q)
$$
仍是原 $\mathcal S_{34}\boxtimes\mathcal S_{18}$ 中的完整来源。
本文给出它的全部偶偶、奇奇张量系数、两个原轴边际、整个普通核心，
以及第一 principal 中央对任意第二输出测试的准确四行返回。

其完整张量秩为十八；第一 principal 来源块秩为四。
原 $S$ 不在这四维来源格中，且这个排除在每个当前普通素数的剩余域
中仍成立。因此不能把 $\mathcal K_1$ 当作原 $\mathcal K_0$ 的相同
中央返回。另一方面，它的原总伴随 core 确实在
$\mathcal K_1,R_Y\mathcal K_1$ 两态中闭合；两态的第一 principal
行准确相同。这为 R442 的完整 carry 消元提供了实际来源关系，
不预付任何新增中央零。

## 1. 同一四挠来源及其原 theta 空间

保持 R439 的固定 ray、$b=17$、sigma、周期和
$$
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad p>19.
$$
记
$$
\Sigma(y,v)=\sigma(y-v)\sigma(y+v),\qquad
\mathcal A_0(y,v)=G_{16}(y)\mathcal R(y,v).
$$
原来源为 $\mathcal K_0=\Sigma\mathcal A_0$。
R439 的精确第二态公式给
$$
\boxed{
\mathcal K_1=\Sigma\mathcal A_1,\qquad
\mathcal A_1=\frac18\sum_{t\in E[4]}
 (T_t^{(32)}\otimes T_{-t}^{(16)})\mathcal A_0.
}
\tag{1}
$$
这里 $T_t^{(32)}$ 是 $G_{16}\mathcal R$ 第一轴的规范乘法 lift。
原 $y=w+9q,\ v=w-17q$、$\sigma(26q)=\sigma(y-v)$ 完整保留。

$\mathcal A_1\in\mathcal S_{32}\boxtimes\mathcal S_{16}$，
而 $\Sigma\in\mathcal S_2\boxtimes\mathcal S_2$。
所以
$$
\boxed{\mathcal K_1\in
\mathcal S_{34}\boxtimes\mathcal S_{18}}
\tag{2}
$$
无平坦 twist，并在当前普通处整。
(1) 同时付两条完整对角零：
$$
W_*\nu_{\mathcal K_1}=V_*\nu_{\mathcal K_1}=0,
\qquad W=Y+X,\quad V=X-Y.
\tag{3}
$$
它不意味着 $\mathcal K_1$ 的两个单轴边际为零。

## 2. 全部十八列的精确多项式

为避免把原物理坐标 $Y,X$ 与椭圆函数混淆，以下写
$$
x_1=x(y),\quad x_2=x(v),\quad y_1=y(y),\quad y_2=y(v).
$$
完整来源为
$$
\boxed{
\mathcal K_1(y,v)=\sigma(y)^{34}\sigma(v)^{18}
 \{P_{\rm e}(x_1,x_2)+y_1y_2P_{\rm o}(x_1,x_2)\}.
}
\tag{4}
$$
没有单独的奇偶或偶奇项；奇奇项一般非零。

下列六个整数矩阵给出全部系数。对于 $r=0,1,2$，列指数依次是
$2-r,5-r,\ldots$，行指数是 $r,r+3,\ldots$。
定义
$$
\begin{aligned}
P_{\rm e}(x,z)
 &=\frac1{252}\sum_{r=0}^2\sum_{a,c}
    E_r[a,c]\,b^{7-a-c}x^{r+3a}z^{2-r+3c},\\
P_{\rm o}(x,z)
 &=\frac1{252}\sum_{r=0}^2\sum_{a,c}
    O_r[a,c]\,b^{6-a-c}x^{r+3a}z^{2-r+3c}.
\end{aligned}
\tag{5}
$$
矩阵大小确定各和的范围。唯一形式上可能出现负 $b$ 次幂的
$E_2[5,3]$ 准确为零。

$$
E_0=\begin{pmatrix}
8192&-20480&-1024\\
-51200&-120832&6400\\
238592&56704&32384\\
-45952&21568&5744\\
-27008&22808&460\\
2000&832&-7
\end{pmatrix},\qquad
E_1=\begin{pmatrix}
81920&90112&35840\\
464896&63488&203392\\
238592&19840&151040\\
-41344&19840&22736\\
-1664&-664&-6560\\
272&-284&119
\end{pmatrix},
$$
$$
E_2=\begin{pmatrix}
-90112&-407552&-19456&768\\
-75776&-397312&-128384&-2112\\
-37888&-60800&-37312&-4464\\
-10624&-163328&-61072&480\\
6592&12656&5104&-123\\
-16&-32&11&0
\end{pmatrix}.
\tag{6}
$$
$$
O_0=\begin{pmatrix}
24576&24576\\
325632&132096\\
199680&140928\\
104064&15936\\
-4416&8760\\
96&-12
\end{pmatrix},\qquad
O_1=\begin{pmatrix}
-49152&-24576&-3072\\
-362496&-43008&-8832\\
-129024&-54144&2304\\
41856&46848&-624\\
-2496&-4920&60
\end{pmatrix},
$$
$$
O_2=\begin{pmatrix}
24576&-6144&-58368\\
43008&-79872&-77952\\
-18432&-109440&-23616\\
-36480&-34944&-4080\\
384&768&-48
\end{pmatrix}.
\tag{7}
$$
因此 (4) 是原 theta 基中的完整张量分解；(5)–(7) 指定每个系数，
并非仅在原点截取若干阶。

## 3. 完整四挠计算的特征零证明

本节说明 (4)–(7) 如何从 (1) 的真实 lift 得到。
先取 $b=1$，令
$$
q_0=1+\sqrt3,\quad q_0^2=2q_0+2,\quad
e=-q_0,\quad h=-1,\quad F=-6q_0-3.
$$
取一个 $t\in E[4]$，使 $x(t)=e,\ y(t)=f,\ f^2=F$、
$x(2t)=h$。令 $\tau=f\,y(z)$，所以
$\tau^2=F(x^3+1)$。

R419 已从原切线除子和半周期归一支付
$$
c_t^8=\frac{1-q_0}{12F}=:k_t,\qquad
c_t=e^{-\eta_t t/2}\sigma(t).
\tag{8}
$$
同一个规范的四次比准确化简为
$$
R_t(x,\tau)
=\frac{\sigma_t(z)^4}{\sigma(z)^4}
=x^2-q_0^2x-2q_0+\frac23(1-q_0)\tau,
$$
$$
x(z+t)=
\frac{-q_0x^2+q_0^2x+2-2\tau}{(x+q_0)^2},
\qquad
\sigma_t(z)=e^{-\eta_tz}\frac{\sigma(z+t)}{\sigma(t)}.
\tag{9}
$$
例如 R419 的原切线表达
$(y+f+3e^2(x-e)/(2f))^2/(x-h)$，
用 $F+\tfrac32q_0^2(x+q_0)=3(q_0+1)(x+1)$，
直接化为 (9)。完整式
$R_t(x,\tau)R_t(x,-\tau)=(x+q_0)^4$
也在显示的二次商环中准确成立。

写 R424 的已证完整多项式为
$$
\mathcal A_0
=\sigma(y)^{32}\sigma(v)^{16}P_A(x_1,x_2),\qquad
P_A=-\frac2{21}x_1(x_1^3+1)(x_1^3-8)\mathcal B_1(x_1,x_2).
$$
$\mathcal B_1$ 是 R424 的整个 bidegree $(8,8)$ Bezout 多项式。
由 (8)–(9)，一条实际反向四挠项除去 frame 后恰为
$$
k_t^6R_t(x_1,\tau_1)^8R_t(x_2,-\tau_2)^4
       P_A(x_{1,+},x_{2,-}).
\tag{10}
$$
$\tau_i^2=F(x_i^3+1)$，且 $\tau_1\tau_2=Fy_1y_2$。
幂次 $6,8,4$ 分别来自原 $c_t^{48}$、degree32 和 degree16；
没有可自由选择的八次根相位。

按 (9) 替换后，所有显示分母在这个完整商环中整除。
可先精确计算 $R_tx_t$、$R_tx_t^2$ 三个 degree4 多项式，
再用
$$
R_t^{N/4}x_t^{2j}=(R_tx_t^2)^jR_t^{N/4-j},
$$
$$
R_t^{N/4}x_t^{2j+1}
=(R_tx_t^2)^j(R_tx_t)R_t^{N/4-j-1}
$$
形成 $N=32,16$ 的每一列。这给一个有限完整算法，不需任何
点值插值、浮点 theta 或截断阶数。

$\mathcal A_0$ 在反对角二挠下固定，且 (10) 的 $t,-t$ 相差该
稳定子，所以两个单奇部分准确为零；保留下来的两个部分的
$\sqrt3$ 系数也准确为零。同一二挠纤维上的四个点给相同整条来源。

原 $\mathcal A_0$ 在同时 $\mu_6$ 旋转下的型为四。
因此对另外两个非零二挠纤维求和，等价于在 (10) 的完整偶偶、
奇奇多项式中只保 $i+j\equiv1\pmod3$ 的项，并乘三。
四个二挠点则各贡献 $\mathcal A_0$。由 (1)，准确得到
$$
\mathcal A_1=\frac12
 \{\mathcal A_0+3\,\operatorname{proj}_{i+j\equiv1}(T_t\mathcal A_0)\}.
\tag{11}
$$
最后乘回
$\Sigma=\sigma(y)^2\sigma(v)^2(x_2-x_1)$，
逐系数即为 (6)–(7)。

从 $b=1$ 到原 $b=17$，真实同构 $u^6=b$ 给
$\mathcal K_{1,b}(y,v)=u^{-6}\mathcal K_{1,1}(uy,uv)$；
偶偶项的准确权为 $b^{(23-i-j)/3}$，奇奇项为
$b^{(20-i-j)/3}$，正是 (5)。辅助六次根已完全消除。

[完整精确脚本](../scripts/check-r443-residual-quarter-core.py) 在
$\mathbf Q(\sqrt3)$ 的显示商环中支付上述所有整除、两单奇部分为零、
完整系数及下文整数秩。
[全部四挠与张量系数](../scripts/check-r443-residual-quarter-core.json)
保留中间四挠项和最终十八列。计算已在特征零完成，无目标素数扫描。

## 4. 两个完整原轴边际

从 (4) 取原第二输出质量，只读偶偶的 $x_2^9$ 列，得到
$$
\boxed{
Y_*\nu_{\mathcal K_1}=\nu_{A_3},\quad
A_3=-\frac{\sigma^{34}x^2}{84}
 \{41X^4-160bX^3+1488b^2X^2+704b^3X-256b^4\}.
}
\tag{12}
$$
这里 $X=x^3$。它以 $-41z^6/84$ 起，质量零，
却不是原 $S$ 的标量倍数。

取第一输出质量，读 $x_1^{17}$ 行，得到
$$
\boxed{
X_*\nu_{\mathcal K_1}=\nu_{B_{18}},\qquad
B_{18}=\frac{\sigma^{18}}{252}
             (11X^2-32bX-16b^2).
}
\tag{13}
$$
它以 $11z^6/252$ 起，质量也为零，但不是零测度。
(12)–(13) 连同 (3) 是完整函数边际；没有从零质量推出
新的 rank-two 或中央零身份。

## 5. 第一 principal 投影的准确四行

第一轴 $\mathcal S_{34}$ 的型零基为
$\sigma^{34}x^{2+3a}$、$0\le a\le5$。
因此第一 $\mu_6$ 平均严格杀掉整个奇奇块以及 $E_0,E_1$ 两块，
只保 (6) 的 $E_2$。定义四条实际来源
$$
\boxed{
A_j=\frac{\sigma^{34}x^2}{252}
       \sum_{a=0}^5 E_2[a,j]\,b^{7-a-j}X^a,
\qquad E_j=\sigma^{18}X^j,\quad0\le j\le3.
}
\tag{14}
$$
于是整个第一 principal 角投影是
$$
\boxed{\Pi_{Y,0}\mathcal K_1=\sum_{j=0}^3 A_j\otimes E_j.}
\tag{15}
$$
令 $d=p-1$，
$J_{A_j}(u)=\int_{\mathbf Z_p^\times}\langle Y\rangle^{du}d\nu_{A_j}$。
对任意连续完整第二输出测试 $h$，准确有
$$
\boxed{
\int\mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{du}
 h(X)\,d\nu_{\mathcal K_1}
=\sum_{j=0}^3J_{A_j}(u)\int h\,d\nu_{E_j}.
}
\tag{16}
$$
原中央导数就是 (16) 对 $u$ 的导数，没有额外未经证明的消失项。

四条全质量为
$$
\boxed{
A_0(0)=-\frac{4b^2}{63},\qquad
A_1(0)=-\frac{8b}{63},\qquad
A_2(0)=\frac{11}{252},\qquad A_3(0)=0.
}
\tag{17}
$$
第7节的真实 $Y$ core 使各单位质量为
$(1-\lambda)A_j(0)$。前三条在每个当前素数处都是单位，
第四条为零。不得因为 (12) 的边际质量零，就把 (17) 的三个
非零条件质量删除。

特别在 R441 的原完整测试 $h(X)=X^6$ 下，
$$
\boxed{
\Gamma_1(X^6)
=\Omega^6\{720J'_{A_2}(0)-864bJ'_{A_3}(0)\},
}
\tag{18}
$$
其中 $\Gamma_1(h)$ 表示 (16) 的中央导数。
这是因为
$\mu_6(E_2)=720\Omega^6,\ \mu_6(E_3)=-864b\Omega^6$，
其余两项的六次矩为零。相应原条件单位质量是
$$
\boxed{
\int\mathbf1_{Y\ {\rm unit}}X^6\,d\nu_{\mathcal K_1}
=(1-\lambda)\frac{220}{7}\Omega^6\in\mathcal O^\times.
}
\tag{19}
$$
该非零质量不等于 (18) 的中央导数已知。

## 6. 完整张量秩、饱和性和原 S 的准确位置

(6)、(7) 六个整数块的非零 Smith 对角依次为
$$
\begin{array}{c|l}
E_0&(1,1944,31104)\\
E_1&(1,5832,93312)\\
E_2&(1,3,31104,279936)\\
O_0&(12,3456)\\
O_1&(12,864,373248)\\
O_2&(48,3456,746496).
\end{array}
\tag{20}
$$
全部因子只含二、三。分母 $252$ 及 (5) 的 $b$ 对角缩放在当前
普通处均为单位。因此 $\mathcal K_1$ 的完整张量秩是
$10+8=18$，在每个当前剩余域中仍为十八。
第一 principal 块秩恰为四，其来源格在完整第一型零格中饱和。

原 $S$ 在 $b=1$ 的六维基中的 $7S$ 列是
$$
s=(-128,-80,-12,-53,7,0)^{\mathsf t}.
$$
把它加入 $E_2$，准确的非零 Smith 对角为
$$
\boxed{(1,1,81,31104,120932352),\qquad
120932352=2^{11}3^{10}.}
\tag{21}
$$
所以增广秩为五；同一个结论经 (5) 的单位 $b$ 缩放在原 $b=17$
及每个当前剩余域中成立。特别
$$
\boxed{S\notin\operatorname{span}\{A_0,A_1,A_2,A_3\}.}
\tag{22}
$$
由于 $\mu_6$ 型直和，(22) 也排除通过对 $\mathcal K_1$ 的第二
输出任意积分直接抽回一个非零 $S$ 倍数。
它不是对所有后续完整算子或 carry 消元的排除。

R307 的另外两条原秩零来源有已知非零中央质量，但其中央导数
也未因此确定；(12) 本身亦不落在
$\langle S,H_{3,17}-H_{5,17}\rangle$。
具体地，取 $b=1$ 并除去共同 $\sigma^{34}x^2$，常数项和
$X^4$ 项若吻合，只能取 $-P_1/4+(P_3-P_5)/2016$；
它与 (12) 的差准确为
$-9X^3/28-207X^2/7-144X/7\ne0$。
本篇不把六维空间中的额外列认作新的算术目标。

## 7. 原 Y/X/W 的完整核心，含奇奇部分

当前 ray 准确给
$$
g=\pi_0/\bar\pi_0\equiv-1\pmod{68},\qquad
g\equiv19\pmod{36}.
$$
整个 degree34 上，普通反射 $R:F(y)\mapsto F(-y)$ 实现同一个
完整 Heisenberg 自同构。原非零偶锚 $S$ 满足 $K_{34}S=S$，
故 Schur 定标准确给
$$
\boxed{K_{34}=R\quad\hbox{于整个 }\mathcal S_{34}.}
\tag{23}
$$
R426 已付整个 $\mathcal S_{18}$ 的 $K_{18}=-I$。
写 $R_Y\mathcal K_1(y,v)=\mathcal K_1(-y,v)=:\mathcal K_1^R$。
于是
$$
\boxed{
\nu_{\mathcal K_1}|_{Y\in p}
=\lambda[\kappa,1]_*\nu_{\mathcal K_1^R},\qquad
\nu_{\mathcal K_1}|_{X\in p}
=-\lambda[1,\kappa]_*\nu_{\mathcal K_1}.
}
\tag{24}
$$
$\mathcal K_1^R$ 在 (4) 中恰是保 $P_{\rm e}$、反转
$y_1y_2P_{\rm o}$ 的真实来源。

R439 已付 $\mathcal L_1$ 的完整 $W$ core 为 $-\lambda$。
独立的 $\sigma(26q)$ 可与 $W$ trace 交换，故
$$
\boxed{K_W\mathcal K_1=-\mathcal K_1.}
\tag{25}
$$
这里保原总伴随 $Q=9Y-17X$，不是只对零 $W$ 边际使用 core。

## 8. 原总伴随在 K1 与 K1R 中完整闭合

R431 的整个 degree52 公式在原双输入上是
$$
\boxed{
K_W=\frac12\sum_{t\in E[2]}
        T_t^{(34)}\otimes T_t^{(18)}.
}
\tag{26}
$$
偶 degree 的规范二挠 lift 满足 $T_{-t}=T_t$，所以 (26)
与 $R_Y$ 精确交换。
由 (25)，$K_W\mathcal K_1^R=-\mathcal K_1^R$。

原 $Y,X$ 同时深与 $W,Q$ 同时深是同一个整坐标域；
行列式为 $-26$。比较两个完整输出核心后，使用
$K_{18}=-I,\ K_{34}=R$，得到
$$
K_WK_Q\mathcal K_1=-R_Y\mathcal K_1.
$$
整个 $K_{52}^2=I$ 已在 R431 支付，所以准确有
$$
\boxed{K_Q\mathcal K_1=\mathcal K_1^R,\qquad
K_Q\mathcal K_1^R=\mathcal K_1.}
\tag{27}
$$
这没有另用未定的 degree7956 标量。

令
$$
P_Q=I+\frac{\kappa-1}{26}
       \begin{pmatrix}9&-17\\-9&17\end{pmatrix}.
$$
(27) 的完整原测度式是
$$
\boxed{
\nu_{\mathcal K_1}|_{Q\in p}=\lambda(P_Q)_*\nu_{\mathcal K_1^R},
\qquad
\nu_{\mathcal K_1^R}|_{Q\in p}=\lambda(P_Q)_*\nu_{\mathcal K_1}.
}
\tag{28}
$$
它保 $W$ 的任意连续测试。偶偶来源和奇奇来源分别有
$Q$ core $+\lambda,-\lambda$，而各自的 $W$ core 都为 $-\lambda$。
相反输出 $V=X-Y$ 的 core 也为 $-\lambda$，由
$R_Y$ 对 (26) 的真实共轭立即得到。

## 9. 两态的原 principal 行严格相同

第一 principal 测试在 $Y\mapsto-Y$ 下固定，且不改变 $X$。
因此对任意连续 $h$ 和整条权参数 $u$，准确有
$$
\boxed{
\int\mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{du}
 h(X)\,d\nu_{\mathcal K_1^R}
=\int\mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{du}
 h(X)\,d\nu_{\mathcal K_1}.
}
\tag{29}
$$
特别两态的中央导数行都是 (16)–(18)。
这是由完整奇奇部分在第一 principal 投影下消失而证明的，
不是只由两个相同边际推得。

所以 R442 中若保留完整来源余项
$\eta\lambda^2(\mathcal K_1-\mathcal K_1^R)$，
只有在同一个第一 principal 测试后，它才严格为零。
(29) 可合法用于原 carry 矩阵，不要求先给 $\Gamma_1$ 赋中央零。
原 $J'_S(0)$ 只控制 $\mathcal K_0$ 的已证条件行；(22) 表明
不能将其未经证明地直接传给 (16)。

## 依赖

- [R419：真实四挠切线比与八次半周期常数](R419-original-opposite-quarter-translates-and-zero-new-total-marginal.md)。
- [R424：完整对称 Bezout 核和原 G16](R424-original-half-period-bezout-kernel-and-complete-central-disintegration.md)。
- [R426：整个 degree18 的绝对普通 core](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)。
- [R431：原 degree52 算子和完整正交坐标](R431-original-degree52-full-core-and-fixed-thirteen-ray.md)。
- [R439：同一个实际第二残余态](R439-original-residual-companion-two-state-core-and-exact-depth-comparison.md)。
- [R307：三条已识别的原算术来源](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)。

