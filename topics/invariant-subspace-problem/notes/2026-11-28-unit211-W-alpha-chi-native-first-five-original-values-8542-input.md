# 新输入：全余 W 五个完整原值先六生成，再单次 α、χ 二列返回

日期：2026-11-28（Asia/Taipei）。Astra-ISP-8542378f-20261127。
源尚未执行；SHA256 71d5dd5050a034a053bacd6d390cac9cabdbb845370f795f9c7731f2aa845235。固定180秒/4GiB。

## 1. 真正新目标与准确范围

此前[全原十行二列](../results/R150-appendix-unit211-W-alpha-chi-exact-original-ten-by-two-and-three-scalars.md)已完整返回。该成功门的十行及三个 scalar 不再执行。新目标是追加五个完整原值条件

$$
q_{T4},\quad R_6,\quad N_{\rm low},\quad P_{\rm low},\quad V_{\rm low}.
$$

它们沿[原低 D 次压缩](../results/R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)与[全域十一原行](../results/R150-appendix-unit211-W-global-D-linear-eleven-original-six-column-return.md)的准确 $D\ne0$ W 范围。个别 N/P 的恢复仍保 NS、PS 和 $R_6$；完整 $N_4(V)$ 不替换成某个分量或 $\Phi$ 倍数。所有计算本身不倒 D、D 的范数、$\chi$ 首项或未付权多项式。

新算法不在先前 $\chi$ 八次行上叠高次范数：先以仅纯权系数的原 native 六生成元处理所有高次原值，最后才一次代入 $(\alpha,\chi)$，按已付首一二次作一次短除。

## 2. 必要定义前缀

只读 a96d 冻结源在 newfive 标记之前的9855 B，SHA

c1436ea6bb67d4c720016091fb65f439be5bfcc7af131c00a0749321fcf45e43。

该前缀只提供新坐标、三原二次与已经证明的实际 $q_\alpha$ 定义。它未进入 native NS/PS 两行构造、原十行清分母或三个成功 cofactor。

其唯一下一层依赖仍是 C9 原源14656 B必要定义前缀，包含真 Gram 和四二次/两三次规则。不会执行旧十八乘法、参数 cofactor、旧函数域门或旧行列式。两个前缀的 alarm/setitimer 都被最外层最初180秒绝对截止钳住；各层地址空间硬界均为4GiB。

## 3. 十二条真实乘法关系与完整原来源 DAG

记 native 六个多项式为

$$
b=(1,x,y,t,y^2,yt)^{\mathsf T},\qquad
F=(E_1,E_{B,e},E_{B,o},N_1,NS,PS).
$$

仅为新原值构造 $\lambda$、$T$ 两个动作的十二条原关系。对每个 $\theta\in\{\lambda,T\}$ 和每个 $b_j$，原 six reducer 实际返回

$$
\sum_i M_{\theta,ji}b_i-\theta b_j
=\sum_a E_{\theta,ja}F_a.
\tag{1}
$$

每个完整多项式乘回由原 reducer 核出；后两原三次的误差系数实际为零。各矩阵系数只有纯权分母，并逐个支付。

后继向量 $r_v$ 仅代表一个真实原多项式 $P_v$，满足
$r_vb-P_v\in(F_0,\ldots,F_3)$，不要求 $b$ 自由。新乘法节点定义

$$
r_{\theta v}=r_vM_\theta.
$$

若旧来源为 $r_vb-P_v=\tau_vF$，完整新来源就是

$$
r_{\theta v}b-\theta P_v
=\bigl(r_vE_\theta+\theta\tau_v\bigr)F.
\tag{2}
$$

源码保存实际父节点、六行系数和十二条已返误差，故 (2) 给出完整可再生来源 DAG；不展开大原乘子，也不将矩阵交换/结合当作自由六维上的恒等式。

每个 $\lambda^aT^b$ 采用固定先 T 后 $\lambda$ 的原乘法次序。独立的二元多项式系数展开只在纯权环中发生。所有加法与纯权系数乘法都按 (2) 合并来源，不倒任何新几何量。

## 4. 五条完整原定义

置

$$
A_\lambda=2\lambda^2-2\lambda+1,\quad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$

$$
D=\ell A_\lambda-T^2,\quad
K=\ell^2B_\lambda-3\ell A_\lambda T+2T^3,\quad
A_0=1+T/\ell.
$$

完整矩式仍为

$$
R_6=MK^2-4m^2D^3.
\tag{3}
$$

为准确固定先前原四次，令

$$
A_* =4uQ-J,\quad
C_* =A_*m^2+J\delta\ell^2,\quad c=3-2\lambda,
$$

$$
a_*=M\ell^2Q(3-4\lambda)+MA_*T^2+
2MuQc\ell T+DC_*,
$$

$$
b_*=2Mm(A_*T+uQc\ell),\qquad
q_{T4}=\frac{2mDa_*+Kb_*}{8muQ\ell^2\delta}.
\tag{4}
$$

(4) 正是已刊原 $C_4$ 除已付权头的定义，不是对新的几何首项求逆；原 qT4 的全部零纤维保留。

令 $n_b,p_b$ 是同一个原 Gram 的 $N_4(g_B),P_2(g_B)$ 的 $\rho$ 奇系数。它们先由完整原函数得到，再经 six reducer 真实返回六行和四原均值来源。新条件为

$$
N_{\rm low}=Dn_b+\frac{2\lambda P_{02}}m KA_0+
\frac{4\lambda P_{02}m}{\ell M}D^2,
\tag{5}
$$

$$
P_{\rm low}=Dp_b+\frac{3P_{02}}{2m}KA_0^2+
\frac{P_{02}(3m^2/\ell^2+\delta)}{2mM}KD+
\frac{6P_{02}m}{\ell M}A_0D^2.
\tag{6}
$$

再用同原 N4 取

$$
V_0=(1,\lambda-1-T,A_0,A_0),\qquad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho),
$$

$$
Z_0=N_4(V_0),\quad Z_2=N_4(V_1),\quad
Z_1=N_4(V_0+V_1)-Z_0-Z_2,
$$

$$
V_{\rm low}=DZ_0+\frac K{2m}Z_1+\frac{D^2}{M}Z_2.
\tag{7}
$$

三个 Z 的 $\rho$ 奇部必须实际全零。源逐条返回它们的完整原六行，故 (7) 是整个原 $N_4(V)$ 的低 D 次输入。

所有五条先经 (1)–(2) 在六生成元中形成；每一条完成即输出小 checkpoint，不等后面的值或标量完成才记录。

## 5. 末次换基、五个新线性式与形式二十行

对每条已返回的六行，只在此时以

$$
b\mapsto(1,x(\alpha,\chi),y(\alpha,\chi),t(\alpha,\chi),
y(\alpha,\chi)^2,y(\alpha,\chi)t(\alpha,\chi))
$$

代入。由于 $x,y,t$ 对 $\alpha$ 一次，得到的多项式 $\widehat P$ 对 $\alpha$ 至多二次。令

$$
q_\alpha=\alpha^2+q_1\alpha+q_0,\qquad
\ell_P=\widehat P-[\alpha^2]\widehat P\,q_\alpha
=r_0+r_1\alpha.
\tag{8}
$$

源实际核完整 (8) 和两个清分母坐标；只有已付纯权公因子可剥，未知 $\chi$ 因子不除。

已有 I6 十行与新五个 $\ell_P$ 及其 $\alpha$ 倍，形式上给出 I11 的二十行两列表示。其中

$$
\alpha\ell_P\equiv-r_1q_0+(r_0-r_1q_1)\alpha
\tag{9}
$$

由相同实际首一二次直接推出。本源实际展开的是五个新两列行；不把 (9) 的五对大系数另称为已经展开或运行。这一准确区分不会影响完整理想的逻辑呈示：每个新生成元的理想在自由二次环境中正是它与其一次 $\alpha$ 倍的基环行空间。

在实际物理原图上仍保 $t,D$ 等局部化。自由秩二只描述首一多项式环境；完整原商的自由性、物理局部化的有限性均不作假设。

## 6. 两个真正新原值标量

仅取两个新同点 pair

$$
(R_6,V_{\rm low}),\qquad (N_{\rm low},P_{\rm low}).
$$

对其两列清分母行 $(a,b),(c,d)$，先精确约掉两个实际乘子 $(d,-b)$ 的公因子，再完整返

$$
\mu_0(a+b\alpha)+\mu_1(c+d\alpha)=C.
$$

因此公因子整零纤维也保留。最后只剥已付纯权支持，任何未付权/几何首项或内容都保持；非恒定结果只是一条原必要关系，不宣全 W 空。

若某个值阶段或 pair 达到资源界，只记录真正完成的原来源与准确退出。不得重启本门或提高预算；已有原十行/三pair不会作为复现门。

## 7. 固定源依赖

1. 2026-11-28-unit211-W-alpha-chi-full-original-ten-by-two-8542.py，完整SHA256
18101a4af587253e1dad49cee60d188c60db401ed34b13cf73edeb4e09b6d42b；
仅9855 B必要前缀。
2. 2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py，完整SHA256
10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1；
仅14656 B必要定义。

所有大结果只有参数定义、次数/项数/字节数与SHA；不保存或传送可重算系数、编码片或矩阵缓存。
