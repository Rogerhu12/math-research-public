# R905 实际认证：七个完整迹对偶连接与五个原 Picard 输入

日期：2026-11-16。本文登记已经完成的公开 Actions 结果，承接 [R905 连接构造](R905-original-bounded-divisor-trace-dual-connections.md)、[R909 完整主部配对](R909-original-full-principal-parts-from-three-coefficients-and-Artin-traces.md) 及 [实际执行方法](../notes/R905-original-trace-dual-connection-consumer-method.md)。

## 1. 已完成结论

在原 $p=41$、原 level82 的负三扭曲曲线 $Y$、原 $\tau,\sigma$、正常基、$c_0,c_1$、极化和 $\kappa$ 下，七个原有界除子

$$
D_1,D_2,D_3,D_4,D_5,X,D_N
$$

的完整正则连接现均已取得准确特征零单位解表达式。每个连接属于
$\mathcal O(H-D)$，在原有理截面 $1$ 中的完整对数主部为 $H-D$。
实际七个 $544\times670$ 主部矩阵的秩均为 $543$，每一个目标的全部
$544$ 条方程都已乘回。这里使用完整有限模，保留所有分歧、幂零厚度以及
$D$ 与 $H$ 的交点。

继而完成原五个
$$
I_{Z_j}=\mathcal O_Y(-Z_j),\qquad j=1,\ldots,5
$$
上的准确正则连接 DAG。原 $Q_N$ 校正先于七次 Galois 平均；最后对完整连接
施加真实曲线半线性对合 $c_Y$。这是原五个线丛上的连接输入，尚未施加原活跃
Hecke 校准，也没有计算非 $p$ 项、Picard 周期或原高度。上述成功不是
“workflow 成功”推定：已读取 actual core receipt、最终证书、全部七份连接证书、
完整单位图与方程阶段、五个输出 DAG。[实际 run](https://github.com/Rogerhu12/math-research-public/actions/runs/43893738459)

数学结果名保持 `R905-original-seven-bounded-divisor-connections-and-five-Picard-inputs`。
特征零对象以同一原系统的准确单位解和函数表达式给出；辅助素点数组没有被改称
特征零展开坐标。

## 2. 原七个来源与共同辅助素点

所有新算术均在实际公开 run 内执行，原辅助嵌入为

$$
\ell=1000000753,\quad
s=99932770,\quad \zeta=549966761,\quad B=3197390.
\tag{905C.1}
$$

正常基次数仍为 $(0,1^{144},2^{127})$。原 $e_i$ 已含 $82^2$ 尺度；
本次没有再次乘除该尺度。七个 $W_D=H^0(3H-D)$ 的来源如下。

| 输入 | 原完成生产者 | 本次所用真实来源 |
|---|---|---|
| $D_1,\ldots,D_5$ | R896，run `43872960726` | 五个最终 normal $690\times418$ 空间、完整证书与各原标记 $Q_j$ |
| $X$ | R872，run `43830071469` | 原 fixed-$\chi$ 完整418空间、除子定义及原 $q_\chi$ 锚 |
| $D_N$ | R894，run `43864869152` | 第16个 flip 的最终418空间、完整证书与完整 $Q_N$ DAG |
| 原曲线和五 $I_Z$ | R849 的 GLOBAL，run `43790410670` | 完整原函数域、Galois、五极理想及 $\eta$ 规范 |
| 原 $W,K,K^{-1}$ | R827，run `43734420663` | 同素点已成 $z=0,1,2,3$ 四个完整272维纤维 |
| 原 $t$ 帧 | R883，run `43843430426` | 原 $t/\rho$ 单位及未缩放帧 DAG |

本次共保留72个原选件：GLOBAL 6、R827 9、R872 8、R883 6、R894 8、R896 35。
旧生产者的完整身份、configuration、manifest 与逐件字节均保在源 inventory，
没有将复制件改写成新数学来源。R827 是原预算终点来源；使用的是该产物中
真实 `complete=true` 的已成阶段，不要求不存在的成功最终证书或顶层 result。

## 3. 七个真实单位图与完整670基

对每个最终 $W_D$，实际从它自身截得
$$
U_D=H^0(2H-D),\qquad \dim U_D=146.
$$
再按原次序从 $W_D$ 补126列。七个来源均在首个辅助纤维 $z=0$ 得到
272阶单位图，认证
$$
\pi_*\mathcal O(3H-D)
 \simeq \mathcal O(1)^{146}\oplus\mathcal O^{126}.
\tag{905C.2}
$$
两侧次数均为146，故实际单位图和原包含关系给出完整丛同构。
七份阶段同时认证 $h^0(H-D)=0$，本次没有进入特殊除子的 fallback。
也没有将“一个模核非零”当作特征零主函数。

实际单位子式如下；表中数值是已成阶段的原字段，未在本地重算。

| $D$ | $\det F_D(0)\bmod\ell$ | 主部543阶子式 $\bmod\ell$ | 完整方程乘回 |
|---|---:|---:|---|
| $D_1$ | 69734280 | 784700897 | 全部544条 |
| $D_2$ | 168135538 | 618599054 | 全部544条 |
| $D_3$ | 994658365 | 348481922 | 全部544条 |
| $D_4$ | 651677365 | 925980972 | 全部544条 |
| $D_5$ | 289814217 | 663501154 | 全部544条 |
| $X$ | 340087577 | 671250156 | 全部544条 |
| $D_N$ | 217513425 | 38773912 | 全部544条 |

令 $\theta_i$ 为 $F_D$ 函数列的原函数域迹对偶，列权为
$\lambda_i=1$（前146列）及 $\lambda_i=0$（后126列）。
相对对偶给出完整基
$$
(z-a)^k\theta_i\,dz,\qquad 0\le k\le2-\lambda_i,
\tag{905C.3}
$$
共670项。准确 $\theta_i$ 是原正常函数域 trace Gram 矩阵与 $F_D^{-t}$
的有限表达式；没有宣称展开了一个新的特征零大逆。实际丛阶段还保留两侧完整
$F_D(0)$ 逆乘回。这里的 $dz$ 是原曲线上的微分；分歧处的正则性由相对对偶
处理，没有将未分歧点计算推广成未证明的完整基。

## 4. 544条完整主部与特征零接受

R909 的完整商为
$$
V_3/(\tau U_D)\simeq H^0(\mathcal O_{D+H}(3H)),
\qquad \dim=544.
\tag{905C.4}
$$
即使 $D\cap H\ne\varnothing$，右侧仍使用相加厚度的有限模。
在 $h_a=\sigma-a\tau$ 的立方平凡化中，对原测试截面 $s$ 的矩阵条目是
$$
M_{s,(i,k)}
 =-[u^{\,2-k}]\bigl(F_D(a+u)^{-1}p_s(a+u)\bigr)_i.
\tag{905C.5}
$$
本次只新增原 $F_D(0)^{-1}$ 的一、二阶逆 jet；零阶直接复用，
两侧乘积模 $u^3$ 均完整核对。这个负号来自把全局留数移到辅助纤维，
与目标 $H-D$ 的方向一并固定。

目标是完整 Artin 迹
$$
b_s=\operatorname{Tr}_{\mathcal O_H}(m_{s/h_a^3})
       -\operatorname{Tr}_{\mathcal O_D}(m_{s/h_a^3}).
\tag{905C.6}
$$
两个代数均保全长度272、剩余域和幂零结构；没有剥掉失败因子。$H$ 侧因
$h_a|_H=\sigma$ 只形成一个共用迹行。每个 $D$ 侧保存完整商、真实循环单位基、
companion 关系及 Newton 迹。七个目标都通过全部146个原商关系，并通过常数测试
$b_1=\deg H-\deg D=0$。

准确主部映射的核为原127维 holomorphic 空间，故秩为543。
实际543阶单位子式证明所选图可用；准确特征零连接的系数定义为同一原543阶系统
的单位解，其余127个系数置零。全部剩余方程在特征零成立的依据是：

1. (905C.3) 是完整670基，(905C.4) 是完整544维主部对偶；
2. 准确秩上界为543，而实际单位子式达到该界；
3. (905C.6) 是原 $H-D$ 的完整对数主部，常数测试为零，全局留数定理保证
   这个准确目标位于像中。

此外，本次还对辅助素点的全部544行作了实际乘回。上述准确接受没有使用
“有限域残差为零就推出任意特征零恒等式”。七份证书均明确
`exact_full_principal_parts_not_only_residues_certified=true`，
`characteristic_zero_connection_coefficients_expanded=false`。

## 5. 七源到五个原 $I_Z$：校正、下降和帧

原参数仍为
$$
(n_j)=(12,8,8,13,14),\quad
(p_j)=(165,93,100,168,371),\quad
(q_j)=(67,67,67,67,134).
\tag{905C.7}
$$
$Q_j$ 是 R896 已标记的原函数，已含 $q_\chi^{-(n_j-2)}$；
本次没有再插入同一负幂。$D_N$ 不被先行称为 $K$ 定义。
实际 DAG 先使用原
$$
T_f^0=(D_N-H)+\operatorname{div}(Q_N)
$$
构造同一原 $\mathcal O(-T_f^0)$ 上的连接，然后取
$$
\beta_N=\frac17\sum_{r=0}^6
 \sigma^r\!\left(\alpha_{D_N,H}-d\log Q_N\right).
\tag{905C.8}
$$
对每个原方向，
$$
\alpha_j^K
 =q_j\sum_{r=0}^6\sigma^r\alpha_{D_j,H}
  +7q_j(n_j-2)\alpha_{X,H}
  -p_j\beta_N-q_jd\log\operatorname{Norm}(Q_j),
\tag{905C.9}
$$
$$
\alpha_j^{\mathbb Q}
 =\frac12\left(\alpha_j^K+c_Y^*\alpha_j^K\right).
\tag{905C.10}
$$
真实 $c_Y$ 保持 $w$、令 $s\mapsto-s$，并按 R860 作
$$
z\longmapsto z-
2\frac{\operatorname{adj}(TI-W)_{0,72}}
        {\operatorname{adj}(TI-W)_{0,0}}\bigg|_{T=w}.
$$
微分和全部函数叶同时拉回；等价地使用已证固定的原 $\nu=dz/g$。
没有用单独系数共轭替换曲线作用。七次 Galois 运输作用于准确系统及完整函数叶，
因此无需再做30个共轭数值连接解。

实际五输出 DAG 共43节点，根为 `alpha_K_j` 与 `alpha_Q_j`，逐项绑定
原 GLOBAL 的两图 `eta_degree_zero_fractional_ideal` 节点。保留原
$\eta_{h_j}=-[I_{Z_j}]/q_j$、原极化、$\kappa$、Hom 字与非零常数来源；
没有换成实下降后的另一条线丛。

在原 $P_0=c_0$：
$$
e_{0,j}=t^{\,7(q_j-p_j)},\qquad
\operatorname{res}_{P_0}\alpha_j=7(p_j-q_j),
$$
$$
\alpha_j\text{ 在 }e_{0,j}\text{ 帧中}
 =\alpha_j+7(q_j-p_j)\frac{dt}{t}.
\tag{905C.11}
$$
所以符号准确相消。实际记录为：

| $j$ | 原 $t$ 帧指数 $7(q_j-p_j)$ | 原截面1中的连接留数 |
|---|---:|---:|
| 1 | -686 | 686 |
| 2 | -182 | 182 |
| 3 | -231 | 231 |
| 4 | -707 | 707 |
| 5 | -1659 | 1659 |

在 $P_1=c_1$，保持原帧1；未来求值时须先在完整连接中相消可去主部。
本次没有求 $P_0$ 或 $P_1$ 的数值连接值。$d\log$ 消掉常数并不授权删除
原 $Q_j,Q_N,t/\rho,\kappa,\nu$ 的刚性化来源，实际输出均保这些引用。

## 6. 实际运行、核心与完整来源

| 项目 | 实际值 |
|---|---|
| repository | `Rogerhu12/math-research-public` |
| run / compute job | `43893738459` / `133391640404` |
| source commit | `f4589d2b0d8f5e2a914ca165a601351d09c303a9` |
| actual core seconds | `48.83139443800002` |
| process / error / complete | `0` / `null` / `true` |
| complete source connections | `7` |
| 完整数学阶段 / current | `87` / `1` |
| configuration SHA-256 | `fe220a1b3216cd28a16d0d3c1916f4660b7708c39a129e8696ba285c2c9e7136` |
| artifact | `14238516346` |
| archive bytes | `67679896` |
| archive SHA-256 | `f4ef0ba08998b69ffd87d7d2bf2fca51701d11a518273a8b7e00071fa3b6cf0a` |
| expires | `2026-11-17T15:14:18Z` |

artifact 名为 `serre-global-R905-trace-dual-connections-43893738459-1`。
完整 ZIP 已纯 IO 核长与 SHA，100个成员与 manifest/reference 完全对应；
98个 manifest 成员逐字节核对。机器输出和原 source carrier 留在一日 active artifact，
Git 中仅登记本文、源码、参数及简明 pins。

固定执行源码：

- core `R905_original_trace_dual_connections.py`：63874 B，
  `d0810c2938bfd6abe1c371bb0d3f1c2b6514fa38c381431c4af84cc9af72a92c`；
- helper `R905_trace_dual_linear_algebra.py`：13831 B，
  `ced5b652ee7124ec45f222c50b8b47a51ba000f0307fc81534f07f59e3f3d2f5`；
- wrapper `R905_public_original_trace_dual_connections.py`：64153 B，
  `ff7ff5f14be18cfe7287fa7615f578f0539e0f2a8a262574371ba52789e236f8`；
- 执行方法：12588 B，
  `a2600cfbc893679ebe9a309f5c4a97da8ef074142a98e5ab1a14fa4d512da52d`。

首 run `43892405424` 仅因原 R827 运输 artifact 名字串错误在导入数学前退出；
本次只修正该真实来源名字。核心、helper、wrapper、方法与数学 tag 规则均未改变，
没有重做首 run 中不存在的数学阶段。

## 7. 实际证书 pins 与后继读取入口

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `p41-original-seven-bounded-divisor-connections-and-five-Picard-inputs-certificate.json` | 17015 | `24045a35dcd878cad48d28aea20bce7077161b0eb9dc86113a54ba83bc71d4a4` |
| `full-outputs-manifest.json`，98项 | 14778 | `b11afeda52eb05af86a6fe162484854c29e0764acb26fb383f3f04d214b63fb0` |
| `R905-original-source-audit.json.gz` | 5896 | `6f9b424f0d23db94da6ec9e3dd9128aaa2c0090c11f68be5c3d7ee63324c98ad` |
| `R905-original-source-inventory.json` | 47487 | `4dd8812eaf287f51fcfd0a84b2c631d4914e6694d7f99cb606d50e6777c22bac` |
| `R905-retained-original-inputs.tar.gz` | 16650321 | `b4b4b46906ee776d50245389b42c8d638d917f95ed49d403ac2525e5e8d14e92` |
| `R905-five-original-Picard-regular-connection-DAGs.json.gz` | 8935 | `e54f41e2ca06279c41dfc9cace8eec6aa3c93f29ad6b660d3aa7536b9a25c28d` |
| 完整 stage manifest（见 FINAL 的 `stage_manifest`） | 10228 | `9ac0f7d37774fb68f74ffec850a2a573e0be724c3b488dae72a0ceb35d1d9f43` |

七个连接证书文件名均为 `R905-<label>-exact-regular-connection-DAG.json.gz`：

| label | 字节数 | SHA-256 |
|---|---:|---|
| D1 | 9989 | `e75bca12f5643bd8ac3c1c2dde2e1646d3de08b9ec17401bdebe601e7851acc8` |
| D2 | 9985 | `a11150caa052882c855e958cbce17f052828957b51bf92eb6ddcece2e44c3e44` |
| D3 | 9988 | `ef77b4549480fbc8c0cd6ba01f21aa9b2dc348484ca3b44aca8bd9d25d86d0ba` |
| D4 | 9986 | `4a605293d2869db3b1e4c70e27dcf2c2fc0575fde97ca99a2bc000bdadc9a176` |
| D5 | 9992 | `b279d40b44a3cf0eeb7fbfe92f13a74ea1313ae226226cc69515e26ef7c037ea` |
| X | 9990 | `9c307f5f3685b3b67b5311a22801b751b6ee2b4114e3bd29db67d7988c328328` |
| DN | 9990 | `77fe659f1ada2459d062dc8d37329c7c35d8e00dac03c01f61deabfc7fc99648` |

每份小证书直接指向原完整418空间和主函数、实际146、272丛图、商模型、
$544\times670$ 矩阵、完整目标及543单位解。后继可按这些准确引用选择最小闭包；
不能仅持一个最终 success 标志就省去实际要消费的单位解或函数叶。

固定证明的真实 SHA：

- R905 原证明：`137f5558857f0c67846fe0e7f32740e569f44c7f2dcb99b9c07b313d18229d7e`；
- R909：`60f74fbd4fd23e64c86df615ee661b874ed8ae900a2c146c26aa74ece28e9391`；
- [原 YP](../notes/2026-11-16-original-Y-RR-connections-and-Hecke-period-row.md)：
  `bdbb6cc590a455a9fba75c378658be69fb19dc1d318c0ec2342edde09e1d06b8`；
- [原 RF](../notes/2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md)：
  `e2b87b990914fe7b47bbbc10348a9f4512dd48da0e28dcddf1883ca42fa232f5`；
- [R860 真曲线下降](../notes/R860-original-adjugate-semilinear-descent-and-rational-differential.md)：
  `7a200b7dd74e1fd51b43e2bac12d277f7b5a3e4fa4161f463bf8c20d51eadf3f`。

## 8. 完成边界

本次七连接及五个原线丛的准确连接表达式已经完成。原127维 holomorphic
不确定性仅按实际543单位图的自由系数置零来固定；尚不是 YP 的原活跃 Hecke
投影校准或 canonical splitting。

实际 FINAL 继续将下列内容记为 false：特征零连接坐标展开；Hecke 校准；原非
$p$ 局部项；Poincaré/Picard 周期；原高度；指定 $T_p$ 非零。没有从这七个连接
推出活跃支持、有限地方项为零、原 A.1 接受或 all-$p$ 首层单位。

本次新算术没有重做旧 $W,K,K^{-1}$、原418空间、$\Gamma$、$\delta B$
或273节点 charpoly；没有新增126个聚合 flip，也没有新增30个共轭数值连接解。
这些减少依赖的是 (905C.8)–(905C.10) 对完整原连接和主函数的准确运输，
并未舍弃其真实帧与后续校准需求。
