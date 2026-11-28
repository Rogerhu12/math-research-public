# 首次输入：正 e、k 首值负二、ell 极点中的完整原两剩余式

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127，GPT-6 Astra Pro（AI-assisted）。

状态：尚未执行的唯一新输入，30秒/256MiB，外45秒。只处理下述新原深中心的同点剩余式，不重跑旧六射线初始理想或任何已冻结目标。

## 1. 先前原范围与新的实际中心

仍为正确 W、完整 b0=0、物理 Dphys非零。已刊正ell排除给 $Z=(k+2)/e$ 整。这里只研究 $\bar k=-2$、ell有极点。记
$$
a=v(e)>0,\quad \beta=u/\ell,\quad b=v(\beta)>0,\quad
B=M/\ell^2=\delta-(\beta-1)^2,\quad
g=4\beta-1+2\beta/k.
$$
原 $b_0$ 给 $T=u\mu/g$，$\mu=2\lambda-3$，$g\to-1$。

从原 q2/R6 的直接阶数比较：$b<a$ 导致
$3n^2-4n+5=3n^2+2n+3=0$（$n=\bar\mu+2$），矛盾；$b>a$ 的mu首值±1也分别由R6唯一最低项或被迫$b=a$排除。这些是新纸面分支，不属于本程序的执行声明。

本次只取剩余中心
$$
b=a,\qquad r=\overline{\beta/e}\ne0,\qquad \mu\in\overline{\mathbb F}_{1009}.
$$
mu极点由原 $R_6/\ell^5\mu^6$ 的首值 $1/(2r)$ 排除。$r=-1$ 时原 q2迫A2首值零，且 $v(B)>a$；原 $D=MS$ 中 S 为单位，R6两项阶差 $2(v(B)-a)>0$，该更深 M 支另由纸证排除。本输入不执行这些已显示的比较，只处理$r\ne-1$、$A_2\ne0$的一般剩余中心。

## 2. 同一点的完整原首项

从完整原定义（blob47281af16fdd0ad7500ecda377c3cb9f9d65e725）直接取首项：
$$
A_2=(\mu^2+4\mu+5)/2,\qquad B_3=(\mu^3+6\mu^2+12\mu+7)/2,
$$
$$
\bar T=-\mu,\quad \bar w=(3\mu+1)/2,\quad
M/\ell\to2(r+1)/r,\quad m/\ell\to-1,
$$
$$
T_0,\Phi\to2/r,\quad P_{02}\to-2/r,\quad
G\to-2\lambda/r,\quad P_c\to4(1+\lambda)/r^2,
$$
$$
V_s/\ell\to1,\quad t_s\to2r(1+\lambda)/(r+1),\quad
y_s\to(1-r)/(2(r+1)),
$$
$$
Z_0/\ell^2\to-\mu(\mu+1),\quad
z_2/\ell\to4/(r+1)-\mu-5,
$$
$$
z_1/\ell\to
\frac{r\mu^2+r\mu-2\mu-r-1}{r+1}.
$$
这是完整原 f 常数系数的首项，不是物理 f=0。N5保原NV/矩的完整必要身份。

原 q2 剩余式是
$$
r(3\mu^2+8\mu+9)+\mu^2-1=0.
$$
置 $f_0=3\mu^2+8\mu+9$、$n_0=1-\mu^2$。由这条原式，$f_0,n_0$ 均非零：若$f_0=0$则$\mu^2=1$但$f_0$分别为20或4；若$n_0=0$则$r=0$矛盾。故
$$
r=n_0/f_0,\qquad r+1=4A_2/f_0.
$$
所有用于计算的剩余分母，只能来自已证明非零的 $n_0f_0A_2$。

设 $R_\mathrm{lead}$、$N_\mathrm{lead}$ 分别为完整原 $R_6/\ell^5$、$N_5/\ell^4$ 的上面首值。程序先严格返回
$$
\frac r2R_\mathrm{lead}=\frac{2A_2}{f_0}F_R,\qquad
n_0N_\mathrm{lead}=F_N,
$$
其中
$$
F_R=2B_3^2-n_0A_2^2,
$$
$$
F_N=n_0A_2(\mu+1)(\mu^2+4\mu+7)
-2B_3(\mu^4+7\mu^3+17\mu^2+25\mu+10).
$$
所以本次确实使用同一完整原N5，不以任意替代多项式搜索空性。

## 3. 唯一小目标与返回范围

在既定素数1009上，只计算这两个新一元原剩余式的完整Bézout。仅移除 $n_0f_0A_2$ 的支持，保原移除尺度；最后实际乘回
$$
A F_R+B F_N=S\,d,
$$
其中 S 仅为已证明非零的剩余因子乘积，d为规范gcd。

只有实际$d=1$与完整两源身份返回时，才可用来排除此明确中心。若d非平凡，则保该中心和所有剩余根；不换素数、重排或改预算追同一目标。原系数、分母与完整乘回均由可读标准Python源码给出，不写大载荷或分片缓存。

源码：2026-11-28-unit211-W-positive-e-k-minus-two-ell-pole-original-residue-bezout-8542.py；SHA256：7a09280436c64f609c275c24b0574d0741956557066081902b07844f72a47f52。
本次未执行；不预报gcd、单位、整ell极点支或任何更大原图的空性。数学运行前实际部分克隆/pull及两README差异检查沿现有驱动。
