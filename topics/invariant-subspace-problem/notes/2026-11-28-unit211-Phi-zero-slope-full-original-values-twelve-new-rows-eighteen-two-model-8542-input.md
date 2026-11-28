# Phi 斜率补图的六个完整原值条件：新增十二行、精确 I10 十八行两列

日期：2026-11-28（Asia/Taipei）。新源尚未执行；120 秒、1 GiB。

## 1. 准确目标与旧来源边界

沿已成
[原 N1 斜率补图精确六行两列](../results/R150-appendix-unit211-Phi-zero-original-N1-slope-exact-six-by-two-presentation-and-three-eighth-degree-scalars.md)，
记当前权环为 $A$，只在明确的 $\Delta_N\ne0$ 补图倒置该权量。原四式
$$
I_4=(q_R,q_W,q_O,q_N)
$$
已严格等价于首一二次环境 $A[\lambda,\mathcal Z]/(P)$ 中的三条线性行及其 $\mathcal Z$ 倍，$P=\mathcal Z^2-\beta_1\mathcal Z-\beta_0$。

本次新增的明确理想是
$$
I_{10}=I_4+(N_S,P_S,R_6,N_{\rm low},P_{\rm low},V_{\rm low}).
\tag{1}
$$
每个新原值先按原三个均值降到 $(1,T,z)$，末尾只作一次原 N1 坐标变化，然后加入其 $\mathcal Z$ 倍。因此本次实际新建十二行，与已成六行合成 (1) 的精确十八行两列呈示。原商不假定自由。没有重建旧三个大 $\lambda^8$ 标量，也没有新大 cofactor 或投影目标。

当前原范围仍是 $\Phi=0,D\ne0$。所有未付权面、整 $\Delta_N=0$、以及其余原 nonzero 条件都保留。理想 (1) 是本文确切对象；不把其某个商中偶然成立的条件称为所有原 admissibility 自动满足。

## 2. 实际原 Gram 与完整加权 N/P

定义保持
[原 U-value atlas](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md)
的归一：
$$
N_4(v)=4N(v),\qquad P_2(v)=2P(v).
$$
置 $\delta=1-Q$、$m=u-\ell$，在 $\rho^2=\delta$ 中保两根：
$$
b=\frac\ell2+\frac{m\rho}{2\delta},\quad
c=\frac\ell2-\frac{m\rho}{2\delta},\quad
a=1-\ell,\quad p=1+\rho,\quad q=1-\rho.
$$
其 $bc=M/(4\delta)$ 是已付原权单位；这里只用明确的 $b^{-1}=c/(bc)$、$c^{-1}=b/(bc)$ 和 $\rho^{-1}=\rho/\delta$，不对扩张取范数逆。

令
$$
G=\lambda P_{02}+(u-1)T_0,\quad
f=\frac{GT_0-QP_{02}(\ell+T)}{P_f},\quad
V=\frac{Jf-G+bc\,z}{Q},\quad
W=\frac{T_0+4uf}{2}.
$$
完整原恢复为
$$
X=\frac{W-qV}{b(p-q)},\quad
Y=\frac{pV-W}{c(p-q)},\quad
t=z/Q,\quad
r=X-ap-ct,\quad s=Y-aq-bt,
$$
$$
A_1=2f-2V+2bc\,t.
$$
原 Gram 行是
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0).
$$
双点乘法与迹保持
$$
(vw)=(v_0w_0,\ v_0w_1+v_1w_0,\ v_Bw_B,\ v_Cw_C),
\qquad \tau(v)=av_0+v_1+bv_B+cv_C.
$$
记 $d=DK(1)$、$F_2=\tau(d)=2f$，则
$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)-4\tau(v)\tau(dv)
 +2F_2\tau(v)^2+\tau(vDK(v)),
$$
$$
P_2(v)=\tau((v-\tau(v)1)^3).
\tag{2}
$$
源码真实构造完整 B 行的 (2)。原 Gram 在 $\rho\mapsto-\rho$ 加 B/C 交换下逐项保持，迹也保持，因此整个 C 行谱就是 B 行谱的共轭；不是删掉 C 的个别条件。

写完整 B 谱为 $N_4(\mathrm{row}_B)=n_e+\rho n_b$、
$P_2(\mathrm{row}_B)=p_e+\rho p_b$。准确加权恒等式是
$$
b(e+\rho o)+c(e-\rho o)=\ell e+mo.
$$
因此新完整加权原式为
$$
N_S=\ell n_e+mn_b-2\lambda P_{02}(\ell+2T+A_2),
$$
$$
P_S=\ell p_e+mp_b-P_{02}(\ell+3T+3A_2+B_3),
\tag{3}
$$
其中 $A_2=2\lambda^2-2\lambda+1$、$B_3=4\lambda^3-6\lambda^2+3\lambda-1$。

## 3. 同一点的矩与个别值条件

记
$$
D=\ell A_2-T^2,\quad
K=\ell^2B_3-3\ell TA_2+2T^3,\quad A_0=1+T/\ell.
$$
完整矩条件是
$$
R_6=MK^2-4m^2D^3.
\tag{4}
$$
其余两个个别原式采用实际完整奇部：
$$
N_{\rm low}=Dn_b+\frac{2\lambda P_{02}}mKA_0
 +\frac{4\lambda P_{02}m}{\ell M}D^2,
$$
$$
P_{\rm low}=Dp_b+\frac{3P_{02}}{2m}KA_0^2
 +\frac{P_{02}(3m^2/\ell^2+\delta)}{2mM}KD
 +\frac{6P_{02}m}{\ell M}A_0D^2.
\tag{5}
$$
置
$$
V_0=(1,\lambda-1-T,A_0,A_0),\quad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho),
$$
$$
Z_0=N_4(V_0),\quad Z_2=N_4(V_1),\quad
Z_1=N_4(V_0+V_1)-Z_0-Z_2.
$$
三个完整二次型的 $\rho$ 奇部实际核为零；保留整个原式
$$
V_{\rm low}=DZ_0+\frac{KZ_1}{2m}+\frac{D^2Z_2}{M}.
\tag{6}
$$
没有把它换成 $\Phi$ 倍数。

这些式的同源意义不依赖 W 图。令
$$
s_U=(\ell\zeta-T)/u.
$$
原两矩给 $Ms_U^2=D$、$2mDs_U=K$，原单值为
$$
h=A_0+(m/\ell-\rho)s_U,\qquad
k=A_0+(m/\ell+\rho)s_U.
$$
完整 N 残式的奇部是 $n_b+4\lambda P_{02}(A_0s_U+ms_U^2/\ell)$；完整 P 残式的奇部是
$$
p_b+P_{02}\bigl(3A_0^2s_U+6A_0ms_U^2/\ell
 +(3m^2/\ell^2+\delta)s_U^3\bigr).
$$
分别乘 $D$ 即为 (5)。整个 $N_4(V_0+s_UV_1)$ 乘 $D$ 恰为 (6)。

在当前原 $D\ne0$ 范围，$s_U=K/(2mD)$ 唯一，(4) 恢复 $Ms_U^2=D$。加权残式是 $\ell$ 倍偶部加 $m$ 倍奇部，$\ell$ 已付，所以 (3)、(5) 恢复 B/C 的两对完整个别 N/P；(6) 恢复整个原 $N_4(V)$。这个 $D\ne0$ 仅用于等价范围，新代数运算从不倒置 $D$ 或 $D$ 的范数。这里也不采用 W 专用的 $q_{T,4}$ 方程。

## 4. 原三均值 DAG 与末尾一次换基

在每个新值的运算中，对两个真实线性余式 $av,bv$，固定乘法取
$$
r=a(b_0I+b_1M_T+b_2M_z).
\tag{7}
$$
原三个规则的实际误差行给
$$
(av)(bv)-rv
 =\sum_i a_i(b_1E_{T,i}+b_2E_{z,i})(q_R,q_W,q_O)^t.
\tag{8}
$$
把输入已有来源归纳组合，即得到每个运算节点的完整原来源。这里不假定 $M_T,M_z$ 在自由三维空间交换或结合，也不要求余式唯一；固定表达式与 (8) 已足够。

新值最后变为三行 $r=(r_0,r_1,r_2)$。令
$$
\kappa=(-cr_1+ar_2)/\Delta_N,\quad
s_0=r_0-\kappa p_0,\quad
s_1=(p_2r_1-p_1r_2)/\Delta_N.
$$
源码返回全部三个系数，所以原新值与 $s_0+s_1\mathcal Z$ 的差属于 $I_4$。再用真实首一二次加入
$$
\mathcal Z(s_0+s_1\mathcal Z)
 \equiv s_1\beta_0+(s_0+s_1\beta_1)\mathcal Z\pmod P.
$$
六个新条件各给两行，恰新增十二行。结合既有精确六行，给 (1) 的完整十八行两列表示。

旧大 $\lambda^8$ 目标未重建；本次没有大 cofactor 或投影。真正新增输入是完整六个原值条件及其同点来源。

## 5. 源身份与两件依赖

建议源文件：
`2026-11-28-unit211-Phi-zero-slope-full-original-values-twelve-new-rows-eighteen-two-model-8542.py`。

源 blob `8c21d65451e9bfeaba96bd822fde99b363d735d5`，12136 字节，SHA256
`527cddc0905e6ab51530b08172fc44c7652926e928de6769603e3a5d037c4c59`。

直接及递归依赖仅两件小源码：

1. `2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py`，SHA256 `c4af169436165777186a811ccbea1b242b64e0bd84ac14bde43289254c4a2332`。只读到 `def add3` 之前的 5809 字节坐标定义，前缀 SHA256 `941f5a6090fbc00bd8eb570efedbbad972d68d90f5a32dfe9c271378740e073c`。可用 `ISP_PHI_SLOPE_SOURCE` 指定。
2. `2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，SHA256 `100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf`，内部仅必要 7097 字节原规则；可用 `ISP_PHI_FIRST_HEAD_RULE_SOURCE` 指定。

两个嵌套 timer 都受本源最初 120 秒截止钳制。输出只包含原定义、次数、项数、SHA 和实际来源返回标记；不保存、编码、分片或输出可重算系数。
