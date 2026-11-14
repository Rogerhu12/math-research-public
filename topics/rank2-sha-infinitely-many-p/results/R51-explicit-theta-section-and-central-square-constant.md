# R51. 实际 theta 因子的显式低阶挠点乘积

日期：2026-11-12。**状态：已证明，两个独立计算证书均已根端复跑；无穷素数条件仍开。**

## 1. 准确截面与全部常数

沿用 $E:y^2=x^3-17x$、$f=34(1+i)$、$Nf=2312$，
$\vartheta^2=x\sigma^2$、$\vartheta(0)=1$。
R49 的实际首项为 $z^4$ 的截面准确为
$$
\boxed{
A(z)=\frac15\vartheta(z)\sigma(z)^{16}
 (x(z)^2+17)(5x(z)^4-34x(z)^2+289)
 =\sum_m b_mz^m.
}
\tag{1}
$$
因此 R49 的三个有理参数为
$$
(u_2,u_3,u_4)=(51/5,-289/5,4913/5).
$$
同一个截面也有准确的低阶挠点乘积式
$$
\boxed{
A(z)=\frac15\vartheta(z)\vartheta(2z)\sigma(z)^2
               \sigma((2+i)z)\sigma((2-i)z).
}
\tag{2}
$$
其零除子为 $4(O)+(T)+[2]^{-1}(T)$，
以及 $E[2+i]\setminus\{O\}$、$E[2-i]\setminus\{O\}$，各点按一阶计；
总次数为 $4+1+4+4+4=17$。

全权中央公式没有剩余的未知代数尺度：
$$
\boxed{
e_m=57800(8\cdot17^3)^{-m}b_m^2\qquad(4\mid m),
\quad 57800=2^3\cdot5^2\cdot17^2.
}
\tag{3}
$$
完整普通反圆分支于是为
$$
\boxed{
F_p^{\Theta,-}(T)=57800f\Omega_p
 (1+T)^{\log_p\langle136\rangle/\log_p(1+p)}J_p(T)^2.
}
\tag{4}
$$
这里 $J_p$ 是 (1) 的实际有界测度在单位上的 principal Mellin 变换，
满足 $J_p(0)=0$；初级有限准确等价 $J_p'(0)\ne0$。

## 2. 第一条证书：全局中央迹的唯一重构

完整代数证明见
[中央迹与准确常数](../notes/2026-11-12-degree17-central-traces-and-square-constant.md)。
在固定 $256$ 点轨道上，以实际 $U_S,x_S,y_S$ 及
$$
DU=-X,\quad DX=2Y,\quad DY=3X^2-17,\quad
C_n=(D+U)^n1,\quad q_j=[w^j]w/\sigma(w)
$$
求
$$
d_m=\operatorname{Tr}
 \frac1{m!}\sum_{j=0}^{m+1}\frac{q_jD^mC_{m+1-j}}{(m+1-j)!}.
\tag{5}
$$
所有多项式都在有理数上准确构造，再在 $3^{400}$ 的有限环里评价。

这不是单凭一个大模数猜全局值。R45 对每个 primitive 导子点给
$$
\begin{array}{c|ccc}
&v(U)&v(x)&v(y)\\ \hline
p\ne2,17&\ge0&\ge0&\ge0\\
2&\ge-3/2&\ge0&\ge1/2\\
17&\ge-3/4&\ge1/2&\ge3/4 .
\end{array}
$$
(5) 中 $U$ 次数至多 $m+1$。
若其实际多项式的公分母为 $D_m$，则
$$
B_md_m\in\mathbb Z[i],\qquad
B_m=D_m2^{\lceil3(m+1)/2\rceil}17^{\lceil3(m+1)/4\rceil}.
$$
已有严格格点界还给
$|U|<740,|x|<50000,|y|<3600000$。
逐项绝对值求和得到有理数 $H_m$，$|d_m|<H_m$；
脚本准确验证 $2B_mH_m<3^{400}$。
因此每个 Gaussian 整坐标在所给界内只有一个可能的剩余类。

实际同一次轨道的 $d_1^{\rm raw}=64(1+i)$
与 R45 的标准值 $64(-1+i)$ 固定唯一的 $\mu_4$ 方向；
没有按不同权分别选符号。所得全局值为
$$
\begin{aligned}
e_4&=\frac{5^2}{2^9 17^{10}},&
e_8&=\frac{97^2}{2^{25}3^2 17^{20}},\\
e_{12}&=\frac{(13\cdot37\cdot67)^2}
 {2^{43}3^4 5^2 7^2 17^{30}},&
e_{16}&=\frac{(2659\cdot10903)^2}
 {2^{59}3^8 5^4 7^2 11^2 13^2 17^{38}}.
\end{aligned}
\tag{6}
$$
由 R49 的准确平方式得到
$$
b_8^2=(1649/60)^2,\quad
b_{12}^2=(9313603/50400)^2,\quad
b_{16}^2=(2421363742117/1297296000)^2.
\tag{7}
$$

## 3. 第二条证书：实际 theta 的严格复区间

完整解析证明见
[Gaussian 与有效分母证书](../notes/2026-11-12-degree17-theta-gaussian-and-denominator-certificate.md)。
它独立固定实际有限角色及方向：
在 $17$ 处取 $i\equiv4$、$\varpi=4-i$，
用两曲线的实际 $5$ 处 Frobenius 值及主 idèle 关系证明
$\lambda(3)=-i$。
$i$ 模 $289$ 的 lift 为 $38$，标准局部 Fourier 核遂给
$$
a_n=
\begin{cases}
\lambda(n)e^{2\pi i\,19n^2/289},&17\nmid n,\\
0,&17\mid n .
\end{cases}
$$
同一个 Hermite 生成函数是
$$
B(t)=e^{-t^2}\sum_{n\in\mathbb Z}a_n
 e^{-\pi n^2/289+2\sqrt{2\pi}(n/17)t}.
$$
记
$$
\Omega_E=\frac{\Gamma(1/4)^2}{2\sqrt{2\pi}\,17^{1/4}},
\qquad c_{17}=\sqrt{\pi/2}\,17/\Omega_E.
$$
R49 的同一尺度给
$$
b_m=\frac{[t^m]B}{[t^4]B}
       \left(\frac{c_{17}}{4-i}\right)^{m-4}.
\tag{8}
$$
全部共同标量在此比值中消去。

有限求和取 $|n|\le350$，用 Arb/Acb 的 $1024$ 位包含区间。
对 $m\le16$，遗漏双边尾小于
$$
12\cdot351^{16}e^{-3\cdot351^2/289}<10^{-500};
$$
最后的不等式由纯整数运算核准。
加上此尾界后，(8) 的三个实际系数均严格为正，
并分别落在 (7) 所列正平方根的 $10^{-250}$ 邻域中。
因此 (7) 的符号全部为正。

解析证书还有一份独立的有理间距证明：
中央微分式给有效整数 $D_m'$，$D_m'e_m\in\mathbb Z$，
严格复界给 $|e_4|<10^{50}$。
R49 已证明 $b_m$ 有理，故其分母至多
$\lfloor\sqrt{D_m'D_4'10^{50}}\rfloor$。
与候选不同的有理数，其间距大于 $10^{-116}$。
所以严格的 $10^{-250}$ 区间本身也唯一确定这三个系数；
没有把浮点吻合提升为未经证明的等式。

## 4. 有限四维空间确定整个实际因子

四个基
$\vartheta\sigma^{16}(x^6,x^4,x^2,1)$
分别从 $z^4,z^8,z^{12},z^{16}$ 开始，首系数均一。
准确三角消元以 $b_4=1$ 和上述三个正系数得到
$$
(1,51/5,-289/5,4913/5).
$$
R49 已证明实际函数就在这个四维空间内，
故这些有限系数确定的是整个实际截面，得到 (1)。

CM division 给
$$
\sigma((2\pm i)z)=
 \sigma(z)^5\bigl((2\pm i)x^2\mp17i\bigr),
\qquad
\vartheta(2z)=(x^2+17)\sigma(z)^4.
$$
代入即得 (2)，也准确核清各个挠点零数。
(6) 又给
$\kappa_Q=e_4(17Nf)^4=57800$，证明 (3)–(4)。

两脚本均已根端全文审查并运行：
[精确轨道重构](../scripts/check-degree17-central-traces.py)
完整重跑约 $15$ 秒；
[严格复区间](../scripts/check-theta-explicit-section.py)
验证所有尾界、区间、分母界及三角求解。
未提交 PDF 或大体积计算数据。

## 5. 无未知有限例外的两个接口

因为 $b_m\in\mathbb Q$，且 (3) 的常数只含 $2,5,17$，
对所有目标普通 $p\ge13,p\ne17$，以及所有惰性 $p\ge7$，
在允许的中央权有
$$
v_pd_m=2v_pb_m.
\tag{9}
$$
普通 $m=p-1$ 时，R40 给 $b_{p-1}\in p\mathbb Z_p$；
$v_pb_{p-1}=1$ 是初级有限的充分证书。
惰性 $m=p+1$ 时，R50 给 $b_{p+1}\in\mathbb Z_p$，并且
$$
\boxed{
b_{p+1}\not\equiv0\bmod p
\ \Longleftrightarrow\ v_pd_{p+1}\le1
\ \Longrightarrow\ \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}.
}
\tag{10}
$$
这里不再有未知系数数域或固定分母带来的例外集合。
(10) 的最后一个箭头仍只是充分条件。

普通处的新测度可以直接取整：
$\Sigma(t)=\sigma(\log_Et)\in t\mathcal O_p[[t]]$，
$x(t)\in t^{-2}\mathcal O_p[[t]]$，
所以 $\vartheta(\log_Et)^2=x(t)\Sigma(t)^2$ 是常数项一的整单位。
奇 $p$ 下其常数项一平方根整，(1) 的四项皆整且至少四阶消失，
唯一额外分母为 $5$，在这些 $p$ 处是单位。
故实际 Amice 变换整，测度范数至多一。
有限挠值对数塔可在这个明确因子上取尾界常数 $B_p=0$：
$$
v_p\!\left(\log_p(1+p)J_p'(0)-L_{p,n}\right)\ge n.
$$
初级有限准确等价某层 $v_pL_{p,n}<n$。
这使证书完全具体，仍未证明无穷多个素数具有这样的层。

## 6. 一个统一到 $D=1$ 的固定系数问题

在 $E_D:y^2=x^3-Dx$ 上用同一多项式形式
$$
A_D=\frac15\vartheta_D\sigma_D^{16}
 (x_D^2+D)(5x_D^4-2Dx_D^2+D^2)
$$
定义首项为 $z^4$ 的截面。
若 $a^4=D$，标准均匀化给
$$
x_D(z)=a^2x_1(az),\quad
\sigma_D(z)=a^{-1}\sigma_1(az),\quad
\vartheta_D(z)=\vartheta_1(az).
$$
因此
$$
A_D(z)=D^{-1}A_1(az),\qquad
[z^{4r}]A_D=D^{r-1}[z^{4r}]A_1.
\tag{11}
$$
对惰性 $p=4r-1\ge7$，$17$ 是单位。
所以 (10) 也可完全等价地研究同一个 $D=1$ 有理级数的
$[z^{p+1}]A_1\bmod p$。
不能把它换成参考曲线自身的 rank-zero theta 因子；这是次数十七的
特定截面，在 $E_1$ 上作同一单位缩放而已。

### 来源

外部 theta 公式、实际局部规范及谱系见 R46–R49；
两篇完整证书写出全局清分母、严格格点界与 Gaussian 尾，不依赖未证BSD。
周期的 beta 积分常数见
[NIST DLMF 19.20.2](https://dlmf.nist.gov/19.20.E2)。
包含区间的算法依据为 F. Johansson, *Arb: efficient arbitrary-precision
midpoint-radius interval arithmetic*, IEEE Trans. Comput. **66** (2017),
1281–1292，[作者原文](https://fredrikj.net/math/arbpaper.pdf)。
