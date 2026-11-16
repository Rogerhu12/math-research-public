# R905 实际消费者：七个有界除子的完整连接与原五 Picard 输入

日期：2026-11-16。本文是 R905／R909 已证明公式的实际执行方法；当前新连接、主部矩阵、Artin 迹和543阶子式均尚未运行。全部新算术只在本公开仓库 Actions 中执行。旧 R896、R872、R894、R827、R849、R883 真实完成来源由完整 manifest、生产者身份和每个选件 SHA 固定。

数学结果名为 `R905-original-seven-bounded-divisor-connections-and-five-Picard-inputs`；最终证书为 `p41-original-seven-bounded-divisor-connections-and-five-Picard-inputs-certificate.json`。成功指七个完整正则连接的准确单位解表达式及五个原 I_Z 的准确连接 DAG；不称原 Hecke 校准、非 p 项、period 或 height 已算。

## 1. 原来源、坐标和七个输入

保持原 p=41、原负三扭曲 Y、level82、原 K 和 L、原 τ、σ、z=σ/τ、全部正常基及同一个辅助素点

$$
\ell=1000000753,\quad s=99932770,\quad\zeta=549966761,
\quad B=3197390.
$$

原正常基次数为 ε=(0,1¹⁴⁴,2¹²⁷)。V_m 的基序逐行列举 (i,k)，0≤k≤m−ε_i；维数 V₁=146、V₂=418、V₃=690。原 e_i 已有82²尺度，消费者不再乘除82²。

七个准确除子来源依次是：

| 标签 | 已完成生产者 | 完整输入 |
|---|---|---|
| D1,…,D5 | R896 真 run43872960726 | 原五 g_j 的最终 H⁰(3H−D_j)，690×418 normal 数组、完整证明、原 Q_j |
| X | R872 真 run43830071469 | `complete-fixed-chi-kernel` 的 `V3_kernel_basis_mod_prime`，原 Dχ 定义和 qχ 锚 |
| DN | R894 真 run43864869152 | 第16个 flip 的最终 normal418、该 flip 完整证书、完整 marked-QN |

这些都是准确 H⁰(3H−D) 的已认证单位解表达式；辅助域数组不是特征零展开。尤其 R894 的 DN 本身不宣称 K 固定。消费者保完整 QN 以及 T_f⁰=(DN−H)+div(QN)，然后才做连接的 Galois 平均。

R896 的五原参数仍为

$$
n=(12,8,8,13,14),\qquad
e=(2970,1674,1800,3024,3339),
$$
$$
p=(165,93,100,168,371),\qquad q=(67,67,67,67,134),
\qquad q_j e_j=1206p_j.
$$

R849 的原完整 global DAG 给相同五 Hom 字、极理想、p/q、Galois 作用、原正常函数域以及未改变的 κ／极化与 η 符号。R883 给实际原 t/ρ 首项。所有这些真实来源一律保留生产者标签和原字节，不把复制件改写为新数学阶段。

R827 消费范围仅原 W／g／h 来源索引及 z=0,1,2,3 四个已经完成的 W、K、K⁻¹。旧 K、逆、W、Γ、δB、273节点 charpoly 和任何原418空间都不重算。旧 R827 的 run 是预算终点而非成功关系证书；完整选中阶段按其真实 `complete=true` 与精确 configuration 核对，result 位于旧 configuration 中。新消费者不要求它具有不存在的顶层 result。

## 2. 从同一个最终418截取146

每个 D 的 U_D=H⁰(2H−D) 必须从该 D 的最终 W_D 截取。实现把690行中的最高272个次数坐标作为 W_D→V₃/V₂ 的矩阵，求一次完整272秩核，保存原自由坐标 identity、实际单位子式、全部272×146乘回。

再用 U_D 的一个实际146行单位子式将其正常 V₂ 坐标归一为这些行上的 identity。该归一只是完整空间的准确换基，不改变原 D、Q、τ 帧或任何原主函数的常数。原 source 矩阵的690×418数值不改变，旧 flip 中属于另一个余因子的146核不冒用为本次 U_D。

这一步的准确性由 deg(2H−D)=272>2g−2 和 R905 的完整 RR 上界给出。若辅助域实际272单位子式未取得，保存真实失败，不能从模核维数推断特征零特殊情况。

## 3. 146／126丛单位图与完整670基

依序取原整数 a=0,1,2,…。在完整正常纤维评价中，把146个 U_D 列放在前，随后按原 W_D 列序补126个独立列。实际272阶行列式为单位后，保存全部低次数 F(z)、F(a) 和唯一这一次 F(a)⁻¹。

前146列权1，后126列权0。两侧丛次数均146，所以真实单位图认证

$$
\mathcal O(1)^{146}\oplus\mathcal O^{126}
\simeq\pi_*\mathcal O(3H-D).
$$

该单位判据同时证明 D 不经过整个 H_a=(σ−aτ)₀，不是只验某一个几何点。π 的分歧、非约化纤维与闭点剩余域不删除。

在原函数域内令 θ_i 为 F 的函数列的迹对偶。准确670基是

$$
(z-a)^k\theta_i\,dz,\quad
k=0,1\ (i<146),\qquad k=0,1,2\ (i\ge146).
$$

θ 的准确表达式使用原正常函数域的 trace Gram 矩阵及 F 的逆转置；特征零可分性和实际单位图保证其定义。消费者保存这条有限矩阵表达式，不冒称展开了庞大的迹对偶函数或一个新特征零 inverse。

若有限 a 前缀没有单位图，消费者保全全部真实 profile，继续其它独立 D。它明确区分：只有准确证明存在 h 且 div(h)=D−H，才能用 −dlog h；一个模一维核不能作此证明。无准确特殊主函数时保留 R905 的两图完整模 fallback 契约，不剥失败纤维、不宣称该 D 的连接已完成。该情况需要真实下一来源或扩大有限前缀，不伪造成功。

## 4. 完整544主部只用三项逆级数

使用 R909 的完整商

$$
V_3/(\tau U_D)\simeq H^0(\mathcal O_{D+H}(3H)),
\qquad\dim=544,
$$

并用 h_a³ 平凡化。采用归一 U_D 的544个原自由行作为商代表；对全部690个原代表形成完整配对，实际核146个关系，再取544行。

只新增 F(a+u)⁻¹ 的1、2阶 Hasse 系数；0阶严格复用上一阶段的 F(a)⁻¹。两侧乘积模 u³ 都完整乘回。矩阵条目为

$$
M_{s,(i,k)}=-[u^{2-k}]\bigl(F(a+u)^{-1}p_s(a+u)\bigr)_i.
$$

负号、列权和 k 范围固定。它来自全局 residue theorem 与完整主部的完美配对。它不是只验证留数，也不是以一条纤维的数据猜测全部极点；D 与 H 相交时，目标仍是相加厚度的完整有限模。

这里没有求 δβ 或新 Γ。低次数多项式系数的 Hasse 平移只是 R909 公式中的底变量展开，不把它当成原正常函数的完整曲线导数。

## 5. 完整 Artin 迹的实际算法

目标为

$$
b_s=\operatorname{Tr}_{\mathcal O_H}(m_{s/h_a^3})
   -\operatorname{Tr}_{\mathcal O_D}(m_{s/h_a^3}).
$$

两个代数都保全长度272及全部幂零厚度。H 侧还有一个共用同一性：h_a|H=σ，故 V₂/(τV₁)、s/h_a、s/h_a³ 的 H 侧矩阵和迹均与 a 无关。只要取得一次真实 H 迹行，它用于全部七个 D；不同 D 换 primitive 参数不会重算已成 H 迹。

D 侧用 V₂/U_D 表示，函数为 q/h_a²。对任意原 r∈V₃，以同一个 F(a)⁻¹执行

$$
c=F(a)^{-1}p_r(a),\qquad
q_r=\frac{p_r-Fc}{z-a},\qquad h_aq_r=r-w_r,\ w_r\in W_D.
$$

保存全部690列的准确多项式除法及完整乘回。这不另求一个分母逆。

固定 primitive 候选 s_n=Σ n^i ℓ_i，其中 ℓ_i 是原146个正常 V₁基，n=1,2,…。一个新 s_n 的正常乘法矩阵具有真实次数界 1+ε_input−ε_output≤3。只在四个旧 W/K/K⁻¹节点形成新列 [s_n,Ws_n,…,W²⁷¹s_n]，右乘旧 K⁻¹，核完整旧 K乘回与交换子。四点插值后核所有节点、全部加权零项；得到同一原权1乘法的模像和准确函数域乘法定义。

这个新乘法用于 H 以及所有实际需要该 n 的 D，只生成一次。对 D 的完整商，矩阵为 Q_D L_h M_s S_D。对 H 则直接取原正常最高次数商。

仅当整个272阶幂基 [1,v,…,v²⁷¹] 为单位时接受该 primitive 参数。保存第272次列、完整 companion 恒等式、两个逆乘回及全部 Newton 迹。若失败，保留完整代数和失败幂基，转下一新的整数参数，不删去某些因子。严格有限存在性依据及小于辅助素数的坏参数界沿 R909；当前有限试次成功仍以实际单位证书决定。

一个完成 trace 行与全部原测试函数的坐标相乘，产生544个目标。不是为544个函数分别求行列式，更不重做原273节点 characteristic-polynomial 生产者。

## 6. 543单位解与准确连接边界

在实际544×670主部矩阵中选择原顺序的543行／列单位子式，另127个系数置零。保存该子式、目标、所选解和全部544行乘回。常数测试函数的目标值为 deg H−deg D=0；全部146商关系也逐一乘回。

准确特征零解是同一原 matrix／target 的543阶单位解表达式。其全部剩余行成立来自完整670基、准确秩上界543、全局留数定理和目标的完整 Artin 迹定义；不是由“有限域乘回为零”推断一个任意特征零等式。

每个成功 D 保存一条 O(H−D) 在原有理截面1中的准确正则连接，完整主部恰 H−D。扩展坐标仍为false，完整主部表达式认证为true。原127维 holomorphic 不确定性由这一次明确的自由坐标零规范固定；这尚不是原 Hecke 投影校准或 canonical splitting。

## 7. 七源直接到五个原 I_Z

DN 的原 QN 先用于

$$
\beta_N=\frac17\sum_{r=0}^6\sigma^r(\alpha_{DN,H}-d\log Q_N),
$$

该平均已经处于同一个原 K 定义的 O(−T_f⁰)。不先将 DN 本身误称 K 定义。每 j 的原 K 连接为

$$
q_j\sum_r\sigma^r\alpha_{D_j,H}
 +7q_j(n_j-2)\alpha_{X,H}
 -p_j\beta_N-q_jd\log\operatorname{Norm}(Q_j).
$$

Q_j 已含原 qχ 的负 (n_j−2) 次幂；不再插入另一个相同因子。所有 q_j、p_j、τ 的权差以及原非零常数原样引用。

最后用 R860 的真实算术对合取 (α+c_Yα)/2。它保持 w，令 s变号，并把

$$
z\longmapsto z-2\frac{\operatorname{adj}(TI-W)_{0,72}}
                         {\operatorname{adj}(TI-W)_{0,0}}\bigg|_{T=w}.
$$

完整微分按同一替换作拉回；等价地，原 ν=dz/g 已被证明固定，只作用于其完整函数系数。绝不以仅共轭正常系数代替 c_Y。Galois 共轭只对已定义的准确矩阵表达式和全部函数叶逐项运输，不重新做三十个数值连接解。

结果逐项绑定原 R849 两图 I_Z 节点。P₀帧仍是 t^(7(q−p))；有理连接留数7(p−q)与该帧的 dlog 正确相消。P₁帧保持1；未求任何数值点值，若未来逐项出现可去极点，必须先在完整连接中相消。R883 真 t/ρ、原 Q_j/QN 的完整标记树和 κ/ν常数均保来源，dlog 消常数不构成删除帧数据的许可。

## 8. 原子阶段、预算和纯IO包装

所有新完整阶段都使用自己的 `R905-*.json.gz` 与新 core/helper/method/source tag。每个成功或失败的有限尝试原子落盘；同 tag 续算直接读取，扩大预算、辅助节点前缀、primitive 前缀或已请求除子数不改变已成数学身份。所有控制量不进入 mathematical tag；固定算法、枚举顺序、原源和证明进入 tag。

输出主链为：来源审计；新公共权1乘法；公共 H 迹；每 D 的146、丛图、h除法／商、两新逆 jet、544×670配对、D迹、目标、543解和准确连接；最后五个原 Picard 连接 DAG。部分终点只记录真正完成项。旧 incomplete FINAL 不束缚新的 current；stage manifest 由实际完整文件和当前断点共同内容命名。

标准库 wrapper 仅作原 source metadata／完整 manifest／选件字节／schema 检查，绝不导入数学 core 或 helper。core 只从公开 Actions 的 CLI调用。外层预算加900秒，先 SIGTERM 后短宽限 kill，写真实124并保完整阶段及最终IO清单；artifact保留一天。Git仅源码、参数、纸面证明和简明运行／SHA登记；机器矩阵、回执、向量和完整产物只在 active artifact／carrier 续传。

最终 `complete=true` 必须同时有七个完整544条主部解和五个原 I_Z 准确连接 DAG。原 Hecke 校准、非 p 局部项、Y period、原高度及指定 T_p 非零全部保持false。

### 固定证明

- R905：`results/R905-original-bounded-divisor-trace-dual-connections.md`，SHA256 `137f5558857f0c67846fe0e7f32740e569f44c7f2dcb99b9c07b313d18229d7e`。
- R909：`results/R909-original-full-principal-parts-from-three-coefficients-and-Artin-traces.md`，SHA256 `60f74fbd4fd23e64c86df615ee661b874ed8ae900a2c146c26aa74ece28e9391`。
- 原 YP：`notes/2026-11-16-original-Y-RR-connections-and-Hecke-period-row.md`，SHA256 `bdbb6cc590a455a9fba75c378658be69fb19dc1d318c0ec2342edde09e1d06b8`。
- 原 RF：`notes/2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md`，SHA256 `e2b87b990914fe7b47bbbc10348a9f4512dd48da0e28dcddf1883ca42fa232f5`。
- R860：`notes/R860-original-adjugate-semilinear-descent-and-rational-differential.md`，SHA256 `7a200b7dd74e1fd51b43e2bac12d277f7b5a3e4fa4161f463bf8c20d51eadf3f`。
