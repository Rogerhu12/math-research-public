# R150 附录：S=0、Lt=0 的原 theta 二次首项零面完整排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-347c-20261126 / unit31_general。日期：2026-11-26。

状态：完整关闭三值互异原图中 $S=0,L_t=0,L\ne0,A_f\ne0,J\ne0$ 且原 theta 二次系数 g2 为零的整个面。全部末 36 个 lambda 参数与两个原二次根同时保留，最后得到原 mean 结果式在完整 72 维代数中的实际逆。未关闭 g2 非零的一般 Lt 图，也没有宣布整个 S 层为空。

## 1. 原参数与两条必要方程

使用已登记的 S0 矩图和原 P1 一次式，作共同规范 $p+q=2$。记

$$
s=2\lambda-3,\quad A=2\lambda^2-2\lambda+1,\quad
C=-4\lambda^2+5\lambda-2,\quad R=3-4\lambda,
$$

$$
D=sC-Az,\quad \Delta=s^2-4z,\quad
B=2Cz-Ds,\quad l=D/z^2,\quad T=C/z,\quad
w=\lambda-1-T.
$$

三值互异给 $z\Delta\ne0$。令 $x=h-1$、$y=k-1$，则 $x+y=s$、$xy=z$；在完整 $d^2=\Delta$ 代数中取 $x=(s+d)/2$、$y=(s-d)/2$，$h=1+x$、$k=1+y$。原参数为

$$
b=\frac l2+\frac{B}{2z^2\Delta}d,\quad
c=\frac l2-\frac{B}{2z^2\Delta}d,\qquad
p=1+\theta d,\quad q=1-\theta d.
$$

两根 d 均保留。设

$$
U=D+\theta B,\quad V=U-z^2,\quad Q=1-\theta^2\Delta,
$$

故 $u=U/z^2,e=u-1=V/z^2$。原 P1 的 t 系数为零恰给

$$
G=z^2(z^2-D)Q-2V(V-z^2)=0.
\tag{1}
$$

这里 G 等于 $z^4L_t/(bc)$。先前完整结论已经支付整个共同规范 u=1、小 J=0、S0 原 P1 双系数同时零、以及 $S=A_f=0,L\ne0$；因此本条保留的图上

$$
eT_0\ne0,\qquad T_0=V_2-2u^2,
$$

以及原 $\lambda,b,c,p,q,p-q,P_0$ 全部非零。

为写清第二条原必要式，令

$$
W=(\lambda-1)z-C,\quad E=D+Cz,\quad T_n=-4V-z^2Q,
$$

$$
Y=2(Ds-Cz)+\theta(Bs-D\Delta).
$$

在 G=0 上，原恒等式给

$$
T_0=T_n/z^2,\quad P_{02}=2P_0=2lQe,\qquad
bpy+cqx=Y/(2z^2).
$$

原 P1 的 f 系数为 $-4e^2T_0/Q$，因而

$$
f=\frac{-T_0^2+2lQ^2(l+T)-2\lambda lQT_0}{4eT_0}.
\tag{2}
$$

将 (2) 返回原 N(V) 条件，清掉仅有的已付因子后，得到

$$
\begin{aligned}
K={}&z^3(R-z)(-T_n^2+2DEQ^2-2\lambda DQT_n)\\
&+8DEQV^2-2VT_nWY=0.
\end{aligned}
\tag{3}
$$

可直接核验：在 (1)、(2) 上，(3) 等于 $2z^7eT_0$ 乘原 $4N(V)$。这些是原 P1 和原第二梯度的兼容式，没有更换 Frobenius 迹或物理配对。

## 2. 原 theta 首项为零时的完整图

写 $G=g_2\theta^2+g_1\theta+g_0$，则

$$
g_0=-(D-z^2)(2D-3z^2),\qquad
g_1=-2B(2D-3z^2),
$$

$$
g_2=z^2(D-z^2)\Delta-2B^2.
\tag{4}
$$

小 J 为

$$
\begin{aligned}
J={}&4z^3+(12\lambda^2-4\lambda-1)z^2\\
&+(96\lambda^3-236\lambda^2+196\lambda-62)z\\
&+192\lambda^4-624\lambda^3+776\lambda^2-442\lambda+100.
\end{aligned}
$$

源码逐项核验两条多项式身份

$$
B^2-\Delta(D-z^2)^2=z^2J,\qquad
g_2=-2z^2J-\Delta(D-z^2)(2D-3z^2).
\tag{5}
$$

在 $g_2=0,J\ne0$ 上，$g_1$ 必非零。若 $2D-3z^2=0$，第二条 (5) 给 J=0；若 B=0，第一式 (4) 与 $z\Delta\ne0$ 给 $D=z^2$，第一条 (5) 仍给 J=0。两者都不可能。

所以每一个本面原点均唯一满足

$$
\theta=-\frac{D-z^2}{2B}.
\tag{6}
$$

没有除掉一个尚未支付的 theta 线性系数。进一步由 (4)–(6)，

$$
u=\frac{l+1}{2},\quad Q=\frac{3-l}{2},\quad
T_0=\frac{1-3l}{2},\quad
bc=\frac{2l^2-l+1}{8}.
\tag{7}
$$

原 $P_0=lQe\ne0$ 支付 $l(l-1)(l-3)\ne0$；原 P1 双系数零面已关闭，故 $1-3l\ne0$。

本条只处理 L 非零、Af 非零图。它们在 (6) 上的分子分别为

$$
L_{\rm num}=2B+s(D-z^2),
$$

$$
A_{\rm num}=Rz(3z^2-D)-(z^4+3Dz^2-2D^2).
$$

因为 $L=dL_{\rm num}/(2B)$ 以及
$A_f=A_{\rm num}/[z(3z^2-D)]$，这些分子是真正已付单位。

## 3. 全部有限参数谱与低谱返回

令 theta 分子为 $-(D-z^2)$、分母为 2B，将原 theta 四次 K 完整齐次代入 (6)。从 g2 和这个代入式中，仅反复剥去如下已付多项式的 gcd 因子：

$$
\lambda,z,\Delta,J,B,D,D-z^2,3z^2-D,z^2-3D,
$$

$$
2D^2-Dz^2+z^4,\quad L_{\rm num},\quad A_{\rm num}.
\tag{8}
$$

得到 F,H，次数与项数为

$$
(\deg_\lambda F,\deg_zF)=(8,5),\quad 33\text{ 项};
$$

$$
(\deg_\lambda H,\deg_zH)=(28,18),\quad 333\text{ 项}.
$$

它们的固定序列 SHA-256 分别为

```
73ea60094d6e71ad6c50f75cb4845c021ca2850ddbd103d5b911a275c0c527b2
5fd9ef8317bbede591fd2f545ab136ca9f42b36bed893dd3c396208de453860f
```

真正的 QQ 结果式 $\operatorname{Res}_z(F,H)$ 为 lambda 144 次。其完整 squarefree 为 43 次，全部不可约因子是

$$
\lambda-\frac{13}{18},\quad \lambda-\frac32,\quad
\lambda-\frac12,\quad
\lambda^2-\frac54\lambda+\frac12,\quad
\lambda^2-\frac12,\quad \Phi_{36}(\lambda).
\tag{9}
$$

Phi36 定义为该完整 squarefree 中唯一的首一 36 次不可约因子；冻结源同时保存其全部 37 个有理系数，并精确验证不可约次数 36。其低次在前系数序列 SHA-256 为

```
52655407a6e3f75884e6eab368a02da55875314d38760241412c130b8b4455e3
```

其余五个因子均完整返回原 F,H，在 $\mathbb Q[\lambda]/(\phi)[z]$ 中求 gcd，再且仅再剥 (8)：

| 原参数谱 | 实际已付共同因子 | 余下 z 次数 |
|---|---|---:|
| $\lambda=13/18$ | 小 J 的一次因子 | 0 |
| $\lambda=3/2$ | z 的一次因子，剥两次 | 0 |
| $\lambda=1/2$ | Delta 的一次因子 | 0 |
| $4\lambda^2-5\lambda+2=0$ 的两根 | z 的一次因子，剥两次 | 0 |
| $2\lambda^2-1=0$ 的两根 | Delta 的一次因子 | 0 |

全部低谱已排除。剩下唯一 Phi36，在完整数域 $K=\mathbb Q[\lambda]/(\Phi_{36})$ 上，原 F,H 的共同 gcd 恰为一个首一 z 一次式。49 次实际域逆均经 extended-gcd 身份和回乘验证。于是全部 36 个 lambda 根上 z 都唯一，没有额外 z 纤维。

实际线性式的常数项是一个 36 系数数域元素；其规范系数序列 SHA-256 为

```
47f80408d54450abf03c354260adb2a68ef30467aa8b5313fee91f776c1993db
```

新原返回源完整保存这 36 个有理数，先核哈希，再将相应 z 返回原 F,H，实际都得零。这样保留真实参数身份，同时不重复先前已完成的 43 秒域 gcd。

## 4. 全部 72 维原代数的真实单位证书

取完整代数

$$
\mathcal A=K[d]/(d^2-\Delta),\qquad \dim_{\mathbb Q}\mathcal A=72.
$$

没有假设第二层不可约，也没有挑 d 的一个根。由 (6)、(7) 及第 1 节公式还原原 b,c,p,q,h,k,w，使用唯一合法的 (2) 得 f。所有原参数分母逐一在 K 中计算真逆，并回乘等于 1。

随后从原乘法、原迹和同一完整 K 重新生成九条 t 多项式。实际原输入身份为

```
823a286bedfe84c89295b4e65d957fbfe0edee41e1502639a0b75dc4fe18bb63
```

原 E0、N0、最高基值、三个 U 矩、原 P(V)、N(V) 都直接校验。原 P1 在全部 72 维代数中确实恒为零；其余八式的 t 次数依次是三条二次 mean、两条三次最高值、一条二次第二梯度 jet、两条三次第二梯度值。这是原剩余系统，没有把只含参数的必要式宣称为充分条件。

令

$$
\mathcal R=\operatorname{Res}_t(E_1,E_B)\in\mathcal A.
$$

一个实际的原有限公共 t 必令此完整 Sylvester 行列式为零，包括首项降次点。执行得到

$$
\mathcal R=\alpha+\beta d,\qquad
n=\alpha^2-\Delta\beta^2\in K^\times.
$$

n 的标准 lambda 多项式表示为 35 次非零元素；由于 Phi36 不可约，n 在 K 中是单位。源码计算 n 的实际 extended-gcd 逆，并在原二次代数中直接验证

$$
\mathcal R\,
\frac{\alpha-\beta d}{n}=1.
\tag{10}
$$

所以原 E1、EB 已无共同 t，整个原系统当然无解。这里使用的是 (10) 这个真正的单位身份；并未把“范数为零”当作原解充分条件。

逆乘子的序列 SHA-256 为

```
55d1a92d6997905c70886c328992212033591823c482f9f1b58d77be4f3ac09d
```

新执行共核验 30 个域逆身份。无需额外线性组合，第一对原 E1、EB 结果式本身已是单位。

这关闭 Phi36 的全部 36×2 参数；与第 3 节低谱合并，限定范围内的整个原 g2=0 面排除完成。

## 5. 两次真实执行身份

第一段完整参数覆盖及低谱返回：

- 源 blob 325607315e93be8280909bd28dbd0db084bebe08，8304 字节。
- 源 SHA-256：621fab03a9961c890fb40603f779747204c255f0fccae15d1d967555cf56cf4c。
- 源提交 f3eb4bac533921bfcaa11becb44d7e9e68cccc3e。
- run 45831444045、job 139948951703；实际 exit2，因整个 Phi36 尚需原方程返回，保留 workflow failure 状态。
- 源 43.666386 秒，driver 43.735470364 秒，峰值子进程 RSS 55188 KiB。
- stdout 57933 字节，SHA-256：ebe67dba625292a269fd6f9e50bd74daf30b8fee4b8316468955adcdc758efcd。

第二段完整原 72 维代数返回：

- 源 blob c7fd69f5a3324be2335648b12287590e27457900，39365 字节。
- 源 SHA-256：0f44821ea3216acf683b72e0c217e1ea9933df2159ec1aed88509de0a723fedc。
- 源提交 f4300897e6d3038fe26b25cf93c91e2f3c9f9cab。
- run 45833519962、job 139956204644，真实 success，exit0。
- 源 4.738630 秒，driver 4.795207189 秒，峰值子进程 RSS 44856 KiB。
- stdout 2258 字节，SHA-256：98ec5cfff4f8144b82a5a4ffa1207ec04707befef040cd94594b14f2e432e25a。

两段均使用 Python 3.12、python-flint 0.9.0。实际 pull 后根 README 和本课题 README 的 blob 仍分别为 282e86b03385d3b6245ce7100ae2e2af7b103c2d、fef43bdf8690f2eec4751d85784a266eacdd0322，无规则差异。新原源使用保留下来的精确参数身份，不重算已排除的低谱。
