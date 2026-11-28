# 全 W 斜率权图的六个同 f 原 NS/PS 四次核与完整 I6

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（UTC）。
- 状态：唯一首次实际完成全部六个新核及完整原来源。
- 范围：整个当前已付 W、原 distinct-singleton、物理 $D\ne0$ 图。$T$ 自由，没有施加 $b_0=0$，没有新增几何头逆。

## 1. 严格结果与准确边界

在[完整六标量原 I4 呈示](R150-appendix-unit211-W-three-pairs-three-same-f-norms-complete-original-I4-presentation.md)的同一点基础上，本篇得到六个非零纯 $(\lambda,T)$ 四次核

$$
\widehat H_{NS,1},\widehat H_{NS,2},\widehat H_{NS,3},
\widehat H_{PS,1},\widehat H_{PS,2},\widehat H_{PS,3}.
\tag{1}
$$

每个新核都完整返回到原六式 $(E_1,E_{B,e},E_{B,o},N_1,NS,PS)$。与既有 $I_4$ 的三 pair、三同 f norm 一起，它们给同一原 $I_6$ 的精确纯 $(\lambda,T)$ 呈示；同一个 $f$ 仍由已刊 $R=f+g$ 唯一恢复。

这是完整原理想的另一种输入。没有新的纯权投影、有限权集合、点数上界或排空结论。原完整 $I_{11}$ 的其余值条件仍保留。六核并不表示任意六维环境自由，也不取代同 f 的三个旧 norm。

## 2. 全域权坐标与实际已付分母

沿旧 $e=u-1$、$Q=ek$、$V_b=uk+2$，令

$$
s=2u-1,\qquad
\nu=\frac{\beta}{u}=\frac{s(k+2)}{V_b},\quad
d=u\nu-s,\quad r=s-\nu.
$$

完整正反关系为

$$
\begin{aligned}
d&=\frac{2s(u-1)}{V_b},&
r&=\frac{s(u-1)k}{V_b},&
k&=\frac{2r}{d},\\
Q&=\frac{2(u-1)r}{d},&
\ell&=\frac{u(\nu^2-(u+1)\nu+s)}r,&
m&=\frac{u\nu(u-\nu)}r,\\
\delta&=\frac{\nu(3u-2)-s^2}{d},&
\Phi&=-2(u-1)(\nu-1),&
J-Q&=-2(u-1)r,\\
T_0&=-\frac{2u(u-1)\nu(\nu-1)}d,&
\beta&=u\nu.&
\end{aligned}
\tag{2}
$$

本次实际全部乘回，且反向恢复旧 W 的 $\ell$。由同一旧原单位可付 $d,r,\nu,\nu-1$，没有新增删图。$\nu+2$ 和 $A_*$ 未被当作全 W 单位，$T$ 没有替换成 b0 的特殊仿射线。

新的小参数定义

$$
P_\nu=(3u-2)\nu^2-(2u^2+3u-3)\nu+(2u-1)^2,
\qquad
P_{02}=\frac{2u(u-1)P_\nu}{d}
\tag{3}
$$

也实际与原 $P_{02}=(2-3u)V_2-Qu+2u^3$ 全部核回。

源的实际分母检查只剥当前已付纯权支持，包括完整原 $2\ell-1$ 排除，及[整个 G36 原曲线排除](R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md)。后者只取已刊 36 项数学定义，再实际返回

$$
d^8G_{36}\!\left(u-1,\frac{2r}{d}\right)
=\sum_{i,j}c_{ij}(u-1)^i(2r)^j d^{8-j}.
\tag{4}
$$

旧 36 项五指数定义 SHA256 为 994fe0821fb8c70e7f82edf8aea19a17ee1ffa99fd5fd4b5b3c065daea84ad78；旧源 blob 为 c489948be8e967575417a1e21de51cd5a915dc80。没有重跑 G36 排除、旧头因式或泛型矩阵，也没有把未付 raw $\det B$ 当单位。

(4) 只是合法使用同一个既有原单位。实际六核的最后已付分子剥除仅在第三个 NS 核和第三个 PS 核各出现一层原 $u$ 支持；未出现额外 G36 分子剥除。全部六个实际原乘子共同因子均为非零有理常数。

## 3. 真 Gram、首一 qf 和原 NS/PS

本次从原 $E_0,N_0,P_1$ 图按同一个 $(\lambda,T,f)$ 恢复 $t,V,W_1,x,y,A_1,r,s$。在完整 $\rho^2=\delta$ 二次代数中直接构造四维真 Gram。

独立 $E_1$ 使用真正 dual 乘法

$$
(vz)_1=v_0z_1+v_1z_0,
$$

因此平方项为 $-4d_0d_1$；没有使用错误 compact E1，也没有偷用 $E_1=E_W$。singleton 行另实际核对含 $2pr$ 的完整平方表达式。

由原均值给

$$
q_f=\frac{bc}{2u(u-\beta)}
 \left(E_{B,e}+\frac{\ell\delta}{m}E_{B,o}\right)
=f^2+q_1f+q_0.
\tag{5}
$$

$u-\beta=u(1-\nu)$ 为旧原单位。对三个原式 $F_i=E_1,E_{B,o},N_1$，设

$$
r_i=F_i-[f^2]F_i\,q_f=A_i+B_if,
\quad
\deg_{\lambda,T}A_i\le2,\quad
\deg_{\lambda,T}B_i\le1.
\tag{6}
$$

与 (5) 一起，它们是原 $I_4$ 的完整双向输入。

原 $NS,PS$ 均由同一完整 Gram 的 $N_4,P_2$ 构造：

$$
\begin{aligned}
NS&=bN_4(B)+cN_4(C)-2\lambda P_{02}(\ell+2T+A_\lambda),\\
PS&=bP_2(B)+cP_2(C)-P_{02}(\ell+3T+3A_\lambda+B_\lambda).
\end{aligned}
\tag{7}
$$

两个 singleton 的共轭关系、(7) 的整个 $\rho$ 奇部为零，及几何总次数至多三，都实际返回。只用首一 (5) 作短除：

$$
F=Q_Fq_f+A_F+B_Ff,\qquad F=NS,PS.
\tag{8}
$$

$\deg_{\lambda,T}A_F\le3$、$\deg_{\lambda,T}B_F\le2$，四次实际短除乘积全部准确返回。没有展开旧大系数 $g$，没有重复旧全十一式或五个 adjugate 三次门。

## 4. 六个新原组合及完整 I6 等价

每个 $F=NS,PS$ 各取三个新组合

$$
H_{Fi}=A_FB_i-A_iB_F
       =B_i(F-Q_Fq_f)-B_Fr_i.
\tag{9}
$$

它们不含 $f$，对 $(\lambda,T)$ 总次数至多四。(9) 直接给全部六原源的显示乘子。实际程序每次清全部六个真实乘子的已付权分母，只有共同因子能同时精除；然后重新把完整原组合乘回，最后只剥原已付纯权支持。

若清分母为 $d_F$、共同因子为 $c_F$，实际恒等式是

$$
c_F\widetilde H_{Fi}=d_FH_{Fi},
\qquad
\widetilde H_{Fi}=\sum_{a=1}^6\widetilde\gamma_aF_a^{\rm orig}.
\tag{10}
$$

所以新核的来源直接由右侧给出；不存在把原方程除未付因子的步骤。共因子零面及所有 $B_i=0$、几何头零面完整保留。

已刊纯权 $R=f+g$ 来源给

$$
\sum_i v_iB_i=1,\qquad g=\sum_i v_iA_i.
$$

记 $P_i=A_i-B_ig$、$P_F=A_F-gB_F$，则

$$
\sum_i v_iH_{Fi}=P_F,\qquad
H_{Fi}=B_iP_F-B_FP_i.
\tag{11}
$$

因而在既有完整 $I_4$ 上，加三个 $H_{Fi}$ 与加原 F 等价。归一后的六核仍有同一双向包含：由 (10) 新核属于原 $I_6$；原 $H_{Fi}$ 又是新核的多项式倍乘旧权单位。因此

$$
I_6
=I_4+
(\widehat H_{NS,1},\widehat H_{NS,2},\widehat H_{NS,3},
 \widehat H_{PS,1},\widehat H_{PS,2},\widehat H_{PS,3}).
\tag{12}
$$

若 $K_1,\ldots,K_6$ 是已刊三 pair、三同 f norm 的 primitive 核，则完整纯几何商为

$$
A_W[\lambda,T,f]/I_6
\cong
A_W[\lambda,T]/
(K_1,\ldots,K_6,\widehat H_{NS,1},\ldots,\widehat H_{PS,3}),
\quad f=-g.
\tag{13}
$$

式 (13) 保全部原重数与同一个 $f$。没有使用新的 $B_i$、raw 行列式或几何首项单位；原 $I_{11}$ 还要加入其余原值条件。

## 5. 实际六核的完整定义指标

所有六核均非零，对 $(\lambda,T)$ 的总次数**恰为四**；单独 $\lambda,T$ 次数也均为四。表中总次数包括权变量 $(u,\nu)$。

| 新核 | $\deg_u$ | $\deg_\nu$ | 总次数 | 项数 | 定义字节数 | 完整原组合秒数 |
|---|---:|---:|---:|---:|---:|---:|
| NS，$r_1$ | 26 | 29 | 40 | 8413 | 249204 | 1.913176055 |
| NS，$r_2$ | 29 | 32 | 44 | 10385 | 319341 | 2.827752839 |
| NS，$r_3$ | 29 | 34 | 45 | 10955 | 338478 | 3.856313125 |
| PS，$r_1$ | 27 | 28 | 41 | 8477 | 249612 | 4.958166918 |
| PS，$r_2$ | 30 | 31 | 45 | 10438 | 318945 | 5.870949967 |
| PS，$r_3$ | 30 | 33 | 46 | 11070 | 343682 | 6.903865727 |

六个定义 SHA256 依序为：

1. 4e392e6a191193cad5a7871d6c95c67e2f586db92dd3685e964d0cecb6695040。
2. b921150d0eeb7933265332951fed70665de70e60340b5ca6cf626d49ea75fcf3。
3. f4b24dbc9ab2ec78f0e67c90c0219fac3188a9d981af169e02deeccec8d8f46d。
4. b816c118e7844e940051070f947d0493e3fa005a3d7ef9b69e68e3103a64f2fd。
5. 58038b0c579c04f057318057e3c91d51cd161b7afbc7c140bd67646f4abfe14d。
6. ca310bc75b45d941e7d35a6ae9e243cb7f0abf15b5317574ea5a161cfecb0e21。

这些可重算大系数不入库；源中定义、哈希和实际小回执足以准确指定它们。本次未作这些核的因式或共同支撑分析，不从次数或项数推断相交为空。

## 6. 唯一首次执行证据

源：

[2026-11-28-unit211-W-inverse-weight-six-small-same-f-NP-original-cofactors-8542.py](../notes/2026-11-28-unit211-W-inverse-weight-six-small-same-f-NP-original-cofactors-8542.py)。

- Git blob：cf6d6f1e31c6c324ac9eea2a5ec179fe70530df0。
- SHA256：758d461e6ce8869e3ff08fc395403f98cce27a1322329e793b21b1bdfb80e131。
- 15990 字节；自含、零依赖；首次 180 秒、4 GiB。
- [完整输入说明](../notes/2026-11-28-unit211-W-inverse-weight-six-small-same-f-NP-original-cofactors-8542-input.md)。
- [小执行回执](../notes/2026-11-28-unit211-W-inverse-weight-six-small-same-f-NP-original-cofactors-8542-execution.json)。

唯一实际 run 46139963439、job 140963504244。源及真实 pull 提交均为 65b8726890b5f7cd6c0cbf3abc6817eae7c9dac6；pull 时间为 2026-11-28 11:27:37.043913 UTC。根 README blob 99c5ad8d06e939e6cfbbab1afdeffa5463f15f18、课题 README blob 5fbd905291dd044c88d35bd9c07ac0e586ff795a，本次均无变。

内层墙钟 7.487228075 秒，最后完整数学阶段 7.410040305 秒，最高 RSS 57880 KiB，exit 0。stdout 21509 字节，SHA256 9e555d1751d64f29b34e5cc891c4d0df6578a99b52c7aa0e634c8d493ad8f0b9。

实际完成 18 次六源完整组合返回、18 次最终 f 系数返回、4 次新 NS/PS 首一短除、605 次精确多项式除法乘回，并支付 53 个不同权分母。这里 18 次组合返回对应每个新核的原始、共同乘子归一、最后已付支持归一三个阶段；不能误读为只检查了 18 个任意数值点。

全部六核及 (12)、(13) 的使用范围明确。没有新增权界或空性结论，也没有改变任何已冻结数学门。
