# R150：纠错后整个 Phi 原 I6 的精确十五列三坐标呈示及两条六次原条件

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

## 1. 结论与原范围

在当前正确 $\Phi=0$、物理 $D\ne0$ 的原图上，沿[整个真实 B 零支排除](R150-appendix-unit211-Phi-zero-true-entire-Bzero-original-exclusion.md) 已支付第一组三条真实均值的完整二次头。因此，以下结论使用纠错后的原式和新实际返回，不恢复任何已撤回的旧紧凑式结论。

设 $\mathcal A$ 为以本篇已付纯权分母局部化的 $\mathbb Q[u,Q]$。在 $\mathcal A[\lambda]$ 上，完整六式原商有精确呈示
$$
\boxed{\quad
\mathcal A[\lambda,T,z]/I_6
\ \simeq\
\mathcal A[\lambda]^3/
\langle G,M_TG,M_zG\rangle ,
\quad |G|=5 .
\quad}                                                    \tag{1}
$$
右侧共有十五个真实原列，基坐标为 $1,T,z$。它是原商的完整呈示，不只是同解集上的裸必要矩阵，也不假设原商自由。

同一实际运行还给两条全图原必要式
$$
C_{\rm NP}(u,Q,\lambda)=0,\qquad
C_{\rm ov}(u,Q,\lambda)=0,                                \tag{2}
$$
两者都对 $\lambda$ 恰为六次。其实际多项式参数如下：

| 原列来源 | $(\deg_u,\deg_Q,\deg_\lambda)$ | 总次数 | 项数 |
|---|---:|---:|---:|
| $N_1,N_S,P_S$ | $(42,22,6)$ | $47$ | $3721$ |
| $N_1,c_1,c_2$ | $(30,15,6)$ | $33$ | $1824$ |

所有乘子共同因子零面均由取消后的真实原组合覆盖。所有新 $\lambda$ 首项零面仍保留。本篇不宣布整个 $\Phi$ 为空，不宣布两条新头互素，也不据此声称所有权纤维已经有限。

## 2. 纯权环、真实三条规则及完整来源

记
$$
s=u-1,\quad \delta=1-Q,\quad K=Q+4s,\quad
L=Q-2s(u-2),\quad \ell=L/Q,
$$
$$
M_n=2uL-L^2-u^2Q,\quad
A=4s^2-Q,\quad
B=-Q^2+(12u^2-20u+8)Q-16s^2.
$$
本次实际系数分母只使用
$$
Q\delta sKLM_nAB.                                      \tag{3}
$$
其中 $A,B$ 的整个原零支已分别排除；$L,M_n,K$ 等来源是正确原权、$P_{02}$、$bc$、$P_f$ 的单位身份。没有额外倒置旧斜率、$\lambda$、$D$ 或几何范数。

三条真实均值记为 $F_0,F_1,F_2$，对应必要定义中的
$R_{\rm true},W_4,O_{\rm true}$。其二次头 $H$ 是纯权矩阵，已刊完整因式为
$$
\det H=\frac{M_n^3L^4AB}{8K^3\delta^4}.                \tag{4}
$$
所以
$$
\begin{pmatrix}q_{TT}\\q_{Tz}\\q_{zz}\end{pmatrix}
=H^{-1}
\begin{pmatrix}F_0\\F_1\\F_2\end{pmatrix}
$$
给真正的三条首一规则
$$
q_{TT}=T^2-\mathbf a\cdot\mathbf v,\quad
q_{Tz}=Tz-\mathbf b\cdot\mathbf v,\quad
q_{zz}=z^2-\mathbf c\cdot\mathbf v,\qquad
\mathbf v=(1,T,z)^t.                                   \tag{5}
$$
反向等式亦由 $H$ 恢复，因此三条归一化规则与三条原均值生成相同理想。

第四原式 $N_1$ 按 (5) 取余为 $\mathbf r_N\cdot\mathbf v$；其减去的部分是实际三个二次头系数乘原规则。已刊正确规则与该余式在本次仅作为必要定义再生，没有再运行旧四头分类或旧斜率开图证明。

## 3. 真动作、两条原 overlap 及四个矩阵缺陷

把规则系数看作列，定义
$$
M_T=[e_T,\mathbf a^t,\mathbf b^t],\qquad
M_z=[e_z,\mathbf b^t,\mathbf c^t],
$$
其中 $e_0,e_T,e_z$ 是三个标准列。对任意两个三坐标向量，先作原多项式乘法，其二次部分按 (5) 约化。这直接给上面两个矩阵的十八个动作坐标；本次已完整返回。

设
$$
[M_T,M_z]=[0,c_1,c_2].                                 \tag{6}
$$
两条列有实际原来源。先取
$$
zq_{TT}-Tq_{Tz},\qquad zq_{Tz}-Tq_{zz},
$$
再减去其真实二次高项乘 (5)，分别得到
$c_1\cdot\mathbf v,c_2\cdot\mathbf v$。源码把这两个完整多项式身份乘回；没有从矩阵形式本身推断它们属于原理想。

写 $\mathbf a=(a_0,a_1,a_2)$，并同样记 $\mathbf b,\mathbf c$。实际返回了全部三十六个坐标：
$$
\begin{aligned}
M_T^2-a_0I-a_1M_T-a_2M_z&=c_1e_z^t,\\
M_z^2-c_0I-c_1^{\rm coef}M_T-c_2^{\rm coef}M_z&=-c_2e_T^t,\\
M_TM_z-b_0I-b_1M_T-b_2M_z&=c_2e_z^t,\\
M_zM_T-b_0I-b_1M_T-b_2M_z&=-c_1e_T^t.
\end{aligned}                                         \tag{7}
$$
第二式中的 $c_1^{\rm coef},c_2^{\rm coef}$ 表示 $\mathbf c$ 的标量系数，区别于 (6) 的两个列。

## 4. 完整原 NS、PS 的同源三坐标返回

原 dual 乘法始终是
$$
(v_0,v_1)(w_0,w_1)=(v_0w_0,v_0w_1+v_1w_0).
$$
原四行 Gram、同一个原 $d$ 和 $F_2=2f$ 给
$$
N_4(v)=2\tau(dv^2)-F_2\tau(v^2)
-4\tau(v)\tau(dv)+2F_2\tau(v)^2+\tau(vDKv),
$$
$$
P_2(v)=\tau\bigl((v-\tau(v)1)^3\bigr).                 \tag{8}
$$
本次按 (8) 的原括号顺序计算，没有把尚未取原理想商的三系数向量当作自由结合代数。

每个二元乘法先保留六个真实系数：
$$
(\text{常数},T,z;\ T^2,Tz,z^2)
=(\mathrm{lo};\mathrm{hi}),
$$
然后输出
$$
\mathrm{out}_j=\mathrm{lo}_j+
 \sum_{i=1}^3\mathrm{hi}_i\,\mathrm{rules}_{ij}.
$$
故每一步原乘积与余式的差正是
$\sum_i\mathrm{hi}_i q_i$，再加两个父节点已有的原差。
独立的动作路径
$$
v_0w+v_1M_Tw+v_2M_zw
$$
又逐坐标返回同一结果。由该局部身份的归纳，整个计算有完整原来源。保留的 DAG 节点只作操作与父节点元数据；源码中的真实系数公式和每步乘回才是来源证据，不宣称仅凭节点编号就有独立的系数证书。

取
$$
A_\lambda=2\lambda^2-2\lambda+1,\qquad
B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1,
$$
计算完整
$$
N_S=bN_4(B)+cN_4(C)-2\lambda P_{02}(\ell+2T+A_\lambda),
$$
$$
P_S=bP_2(B)+cP_2(C)-P_{02}(\ell+3T+3A_\lambda+B_\lambda).
$$
全部奇 $\rho$ 系数真实返回零，余下三坐标为
$\mathbf r_S,\mathbf r_P$。实际次数为
$$
\deg_\lambda\mathbf r_N=(2,1,1),\qquad
\deg_\lambda\mathbf r_S
=\deg_\lambda\mathbf r_P
=\deg_\lambda c_1
=\deg_\lambda c_2=(3,2,2).                             \tag{9}
$$
本次共有 $1590$ 个操作节点、$1974$ 个新乘法坐标返回。没有重放旧完整六原式的大系数展开。

## 5. 十五列的稳定性与完整商同构

令
$$
G=\{\mathbf r_N,\mathbf r_S,\mathbf r_P,c_1,c_2\},
\qquad
\mathcal N=\langle G,M_TG,M_zG\rangle_{\mathcal A[\lambda]}.
$$
式 (7) 使 $\mathcal N$ 同时被 $M_T,M_z$ 保持：
二次动作归回 $I,M_T,M_z$，缺陷项都落在
$\langle c_1,c_2\rangle\subset\mathcal N$。因此一次动作闭包已经足够，不必假定后续动作独立或无限加入新行。

在 $\mathcal E=\mathcal A[\lambda]^3/\mathcal N$ 中，
(6) 使两动作交换，(7) 使三条二次规则都成立。
同时
$$
M_Te_0=e_T,\qquad M_ze_0=e_z,
$$
所以 $e_0$ 是循环向量。完整 $N_1,N_S,P_S$ 按第4节原来源分别归为 $G$ 中的三列，故全部六原式在 $\mathcal E$ 中消失。于是得到从原六式商到 $\mathcal E$ 的满射。

反向把三个标准列送到原商中的 $1,T,z$。所有十五列都有实际原来源：种子由第2–4节给出，动作列是同一个原变量乘这些关系再约化。故该映射在 $\mathcal N$ 上为零。两映射在三个生成元上互逆，得到 (1)。

实际十五列的 $\lambda$ 次数分布为：

| 种子 | 本身 | 乘 $T$ | 乘 $z$ |
|---|---|---|---|
| $\mathbf r_N$ | $(2,1,1)$ | $(3,2,2)$ | $(3,2,2)$ |
| $\mathbf r_S$ | $(3,2,2)$ | $(4,3,3)$ | $(4,3,3)$ |
| $\mathbf r_P$ | $(3,2,2)$ | $(4,3,3)$ | $(4,3,3)$ |
| $c_1$ | $(3,2,2)$ | $(4,3,3)$ | $(4,3,3)$ |
| $c_2$ | $(3,2,2)$ | $(4,3,3)$ | $(4,3,3)$ |

这覆盖整个当前正确图，包括旧斜率为零的所有原纤维。

## 6. 两条新的六次原组合及首项范围

对三个选定原列 $r^{(0)},r^{(1)},r^{(2)}$，取后两个坐标的三个 cofactor $\mu_i$。于是
$$
\sum_{i=0}^2\mu_i r^{(i)}=(C,0,0)^t.
$$
本次先清三个实际乘子的纯权分母，取全部三个分子的 gcd，再逐个精除该共同因子。使用新的三个乘子重新组合原列，完整返回全部三个坐标。因此共同因子为零时新组合仍成立；没有直接把原方程除以未付因子。

对 $(\mathbf r_N,\mathbf r_S,\mathbf r_P)$，实际共同乘子因子总次数为 $2$；对 $(\mathbf r_N,c_1,c_2)$，共同因子是常数。两个原标量分母均为常数。最后只剥 (3) 的原单位支持，得到 (2)。

精确身份由如下哈希固定：

| 对象 | SHA256 |
|---|---|
| $C_{\rm NP}$ | fcf79be98410a2eea2ebdb588b441b8f4aceb20acb4704a96ee34fc0012d01d5 |
| $C_{\rm ov}$ | 2407107501f1790a288ecabd75f14f92c7602859bfc033727b76312675f91014 |
| $h_{\rm NP}=[\lambda^6]C_{\rm NP}$ | 63c05c345cbc7055d652d46c173684bd7fdb159db3741232ef94d6cb58992bf6 |
| $h_{\rm ov}=[\lambda^6]C_{\rm ov}$ | 9794fac2ee8bf7de08d80b9f3102480f1d06c9cfb4ff8be3981817dcfbd682fb |

$h_{\rm NP}$ 的双次数为 $(37,21)$、总次数 $41$、$471$ 项；
$h_{\rm ov}$ 的双次数为 $(24,15)$、总次数 $27$、$230$ 项。
它们是本次返回的真正原头，但未被支付成全图单位。

在 $h_{\rm NP}\ne0$ 或 $h_{\rm ov}\ne0$ 的任一权开图，(2) 中相应式可归为首一 $\lambda^6$。结合 (1)，尚未反演几何 $D$ 的必要原代数在该权环上由
$$
\lambda^j,\ \lambda^jT,\ \lambda^jz,\qquad 0\le j<6
$$
这十八个元素生成。故这些权开图上的每个固定权纤维长度至多 $18$；随后取原 $D\ne0$ 等开条件不增加纤维点数或长度。

不声称反演 $D$ 后仍是同一基环上的有限模；无需倒任何 $D$ 范数。两个新头同时为零的全部权纤维仍保留，也没有从两个非零多项式推出其共同零集有限。

## 7. 唯一实际执行与可再生源

- 原源：notes/2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py。
- Git blob：f73a06b941fe6c990c5d22ebf1778f05e7c76c74。
- SHA256：84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0。
- Run：46130918529；job：140935643723；仅 attempt 1。
- 源提交：498bba413fd82ac2f13b125f5836b151a4eae820。
- 实际 pull 后：8874f0c2fc047cddc2e5a0b67a7ab6f4b2b44f9d，2026-11-28 09:32:19.568220 UTC。
- 两 README 的本次真实比较无变化。
- 数学末阶段：$2.868058455$ 秒；驱动：$2.910171339$ 秒；RSS：$47372$ KiB；exit：$0$。
- stdout：$7326$ 字节，SHA256 7448a444f64326783a8783ff6f1ca7bd00520a163abafd83bd2b6ed178f7643c。
- 完整统计：十八动作坐标、两个原 overlap、三十六缺陷坐标、$1974$ 乘法坐标、六个末 cofactor 坐标、$137$ 次精确整除乘回。

依赖仅为正确四原式源的 $4007$ 字节定义前缀，SHA256
dd105b713040712dad7cebeefb489c8e1cf53f56cb5fce8ff0de0bf681d6c669。
完整依赖源 SHA256 为
5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。
没有执行其旧头分类、旧斜率门或任何已撤回源。

已成结论依据唯一真实返回直接登记；无需附加完整源重放。下一步可以从这两个新原头或同一十五列呈示取得真正新条件，但本篇没有预记这些后续计算。
