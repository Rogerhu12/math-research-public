# R133：真实负型区到共同根片的完整强桥与物理变分端口

**已证明并实际完成。** 本篇补上完整 moving 能量终点 $r=119/500$
到真实共同根片左端

$$r_c=\frac{8584986789675009}{36028797018963968}$$

的外部严格负型区。对象仍是 $\alpha=3/4$、M256 accepted000 的原
完整物理互逆中心，准确
$\nu=-2443457753738987/72057594037927936$，全部原
$|\eta|\le10^{-9}$ 和 primitive 无限尾保留。不是将新 $.765$ moving
候选或别的参数下的计算混入旧数值。

桥包含2条真实闭径向盒、各4096个闭角单元，以及中间和**终点进入根片**
的2个实际 PPoly 接缝。终点右侧确为保存候选的第1015片。根的完整
区间严格在 $r_c$ 右侧；本篇不延伸进该共同解析片，也不把根图的
$T=\text{常数}$ 曲线口当作固定 $r$ 圆。

完整 moving $H^1$ 初值传播正向小于 $1.414932$、反向小于
$5.791178$；完整 $L^1_rH^1$ 普通源分别小于 $1.415526$ 和
$5.791644$。全部均值行与 Fourier 变分同时保留。随后给出终点
moving 变分到原物理角变分的真实 $H^0/H^1$ 矩阵，所有角密度和逆图
导数都显式付费。

## 1. 真径向盒、目标与同一个解析片

紧支撑目标变化在 $.18$ 之后准确消失，所以整个本桥用原完整目标
$E,a,K$，而不是用旧目标近似新的支持内部。新的原生计算逐盒重新消费
`CodazziCoefficientTarget` 的完整 primitive 与全参数包络，先证明
$K<0$ 和 $E-a'^2>0$，再形成 $q=\sqrt{-K}$、$s=1/C_r$。

实际两个闭盒为

$$
\left[\frac{119}{500},\frac{2144839322535199}{9007199254740992}\right],
\quad
\left[\frac{2144839322535199}{9007199254740992},r_c\right].
\tag{B.1}
$$

候选片号依次1013、1014；另在 $r_c$ 以右侧1015片重新求一个真实点迹。
每一盒均含在同一实际 scalar germ

$$
\left[\frac{8556839292003943}{36028797018963968},
\frac{8636031980136455}{36028797018963968}\right].
$$

候选 Fourier/PPoly 完整 SHA、真实节点、原 primitive 输入和之前完整
能量的目标身份在程序中相接。终点右侧的完整候选片为

$$
\left[r_c,\frac{4295308144604611}{18014398509481984}\right],
\tag{B.2}
$$

它与已付的紧根盒严格相容。该片内部的实际复域、fold 和 Airy 是另一个
同对象接口；本篇不从两个外部闭盒推出其复域。

## 2. 三态完整强传播与两处接缝

直接使用[完整强能量](R133-supplement-actual-moving-H1-and-fractional-full-source.md)
的三态 $(E_0,M,E_1)$，其中

$$E_j=\|H^{1/2}\partial_\phi^jh\|_2,\quad
H=\operatorname{diag}(1,-K),\quad M=|\langle h_2\rangle|.$$

真 $D,m,R,L,L_2$ 均由各盒的同角格四则运算求得；完整五阶角 Taylor
费用和显式三角和算术保持原样。所有子区间的正向充分矩阵为

$$
U_f\le\begin{pmatrix}
1.000000005&0.000121041&0\\
0.000081723&1.000050821&0\\
0.001191104&0.000685606&1
\end{pmatrix};\tag{B.3}
$$

反向为

$$
U_b\le\begin{pmatrix}
4.093716841&0.000220886&0\\
0.000213830&1.000000009&0\\
0.004875922&0.001249677&4.093569374
\end{pmatrix}.\tag{B.4}
$$

这里对角仍按已经证明的方法与0取较大值，以使完整有序积控制任意
内部源插入点。真实有符号终点矩阵另存报告。由真实初值
$M_i\le E_{0,i}/q_i$ 和全盒 $q$ 下界得到开头的 $H^1$ 费用；
$H^0$ 初值增益正向小于 $1.000991518$、反向小于 $4.096344478$。
所有 $0\le s\le1$ 的同阶 Cauchy/source 界仍用完整两端 Hilbert
插值，不截断 mean 或非零模式。

物理接缝由原 dyadic PPoly 完整左右迹精确求得。先支付同一个 $\phi$
上的中心跳，再使用强能量 S.13 支付一阶角跳。**终点**进入1015片的
跳也在前向终点加入；反向则在首次负向传播前加入。两跳总的完整强费用
正向小于 $9.407\cdot10^{-17}$，反向小于 $3.851\cdot10^{-16}$。
零阶相应小于 $6.792\cdot10^{-18}$ 和 $2.781\cdot10^{-17}$。
因此在 $r_c$ 接线时不存在未支付的最后一个 PPoly 接口。

## 3. 固定径向端口的准确变分逆

以下仅在一个真实固定 $r$ 圆上转换端口，不假设中心已满足 PDE。
令 moving 变分为 $h$，$z=\langle h_2\rangle$，并取同一反射角原点。
由已经证明的完整变分桥，原物理角变分拉回到 $\phi$ 后准确为

$$
k=h-Q_\phi\chi,\qquad
\chi=\frac1v I\left(h_2-\frac{zv}{m}\right),\quad m=\langle v\rangle.
\tag{B.5}
$$

这里完整均值项是可逆性所必需。设真实端口上
$g\le|v|\le V$、$m_-\le|m|\le m_+$，并记
$V_2=\|v\|_2$、$V_\phi=\|v_\phi\|_\infty$。
四重原函数的范数 $1/4$ 给

$$
\|\chi\|_2\le aE_0+bM,\qquad
a=\frac1{4gq},\quad b=\frac{V_2}{4gm_-}.
\tag{B.6}
$$

从 $v\chi=I(h_2-zv/m)$ 准确微分，而不是形式丢掉均值，可得

$$\chi_\phi=h_2/v-z/m-(v_\phi/v)\chi,$$

所以

$$
\|\chi_\phi\|_2\le E_0/(gq)+M/m_-+(V_\phi/g)(aE_0+bM).
\tag{B.7}
$$

由 (B.5)–(B.7)，令 $W=L_2+LV_\phi/g$，得到同一 $\phi$ 测度下

$$
\begin{aligned}
\|H^{1/2}k\|_2&\le(1+La)E_0+LbM,\\
\|H^{1/2}k_\phi\|_2&\le
[L/(gq)+Wa]E_0+[L/m_-+Wb]M+E_1.
\end{aligned}\tag{B.8}
$$

原物理角并不是该计算角。实际
$\theta_\phi=v/m>0$ 和 $\partial_\theta=(m/v)\partial_\phi$ 给

$$
\|H^{1/2}k\|_{L^2_\theta}\le\sqrt{V/m_-}\|H^{1/2}k\|_{L^2_\phi},
$$
$$
\|H^{1/2}k_\theta\|_{L^2_\theta}\le
\sqrt{m_+/g}\|H^{1/2}k_\phi\|_{L^2_\phi}.
\tag{B.9}
$$

这同时支付真实测度、逆角链式法则和角导数；没有把原物理范数和
moving 范数直接等同。

## 4. 真终点的数值端口与适用范围

完整右侧点盒给

$$q(r_c)>0.08406225068,\quad |v|>0.50371198599,\quad
|v|<1.77058124124,$$
$$L<2.53896896237,\quad L_2<13.79323988299,\quad
V_2<1.20475680382,\quad V_\phi<2.49340321804.$$

真实 $m$ 也保留其全参数和角平均误差。将它们代入 (B.8)–(B.9)，完整
有向程序得到

$$
\boxed{
\begin{pmatrix}
\|H^{1/2}k\|_{L^2_\theta}\\
\|H^{1/2}k_\theta\|_{L^2_\theta}
\end{pmatrix}
\le
\begin{pmatrix}
20.109029668&1.705263634&0\\
321.439157178&24.371140757&1.490888291
\end{pmatrix}
\begin{pmatrix}E_0\\M\\E_1\end{pmatrix}.}
\tag{B.10}
$$

这是仍带 $H(r_c)$ 的物理端口。若下一算子要求普通未加权
$(\delta u,\delta v)$ 的 $H^s_\theta$，必须额外乘
$\max(1,q(r_c)^{-1})<11.896$；不得把它免费删掉。需要分数阶时，先由
(B.10) 和真实 $M\le E_0/q$ 得同一端口算子的 $H^0,H^1$ 界，再按相同
标度插值。保留完整三列通常比提前吸收均值更紧。

本篇的齐次径向传播仍是 moving 方程自身的线性化。对原物理 Jacobi
在一个未解 PDE 的中心上作同一连接时，还必须保留完整
$H''[R,k]$ 残差桥和实际跨片接口；(B.10) 只给固定圆的准确代数端口，
没有暗中令残差为0。同样，根图的实际 $T(X)$ 端口需要另付曲线 trace，
不能把 (B.10) 的固定 $r_c$ 当作常数 $T$。

## 5. 可复跑文件

源码：`scripts/fourfold_codazzi_strict_to_root_germ_bridge.py`。
完整原生：`notes/2026-11-13-R133-strict-to-common-root-germ-alpha075-native.json.gz`。
该报告完整保存2条闭盒、右侧点迹、2个真实跳、双向三态矩阵及 (B.10)
未外放的有向数值；实际正常完成约5.23秒。所有输入和依赖 SHA 在报告
中保留，无需额外大中间文件。

主调用为

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_codazzi_strict_to_root_germ_bridge.py --candidate /workspace/scratch/ac0d699811ad/reciprocal-m256-alpha075-accepted000-candidate.json --out notes/2026-11-13-R133-strict-to-common-root-germ-alpha075-native.json.gz
```

这是严格负侧与同一个实际共同根片的完整接口；完整高频返回逆、真正
正帽和 regular 外尾仍须联立，不由本桥单独推出混合边值可逆。
