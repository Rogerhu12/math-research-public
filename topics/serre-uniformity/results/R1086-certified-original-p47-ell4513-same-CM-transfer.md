# R1086：原 p47 八个 CM 标签在 4513 的完整同点转移

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
状态：**已证明；新公开精确计算成功。**

原曲线 $X=X_{\rm ns}^{+}(47)$ 在 $\mathbf F_{4513}$ 上有
$5453$ 个点。原完整十角色 Kummer 标签在这些点上单射。
因此，R1074 已留下的任一全局有理点，与其原 $47$ 圆盘的那个
有理 CM 点，在 $4513$ 约化为**同一个原曲线点**。

本篇消费旧八个全局标签，不重报旧 $283$ 排除的 $227$ 个圆盘。
它不证明八个原圆盘内部的有理唯一性；Serre 主目标仍 OPEN。

## 1. 实际公开回执与完整输入

- source commit：
  [19c70348436029da6bafade64e8c2e296fde96a5](https://github.com/Rogerhu12/math-research-public/commit/19c70348436029da6bafade64e8c2e296fde96a5)；
- [run45938730258](https://github.com/Rogerhu12/math-research-public/actions/runs/45938730258)，
  [job140307865125](https://github.com/Rogerhu12/math-research-public/actions/runs/45938730258/job/140307865125)，
  attempt 1，全部步骤及 job 均 success；
- 数学耗时 $60.839069453$ 秒，总预算 $600$ 秒、预留 $30$ 秒；
- python-flint $0.9.0$，exact integer/finite-field arithmetic；
- 运行前核实际 HEAD=GITHUB_SHA、公开仓库、请求、源码及两 README 的 SHA。
  root 与 global_route 在提交前已全文纸审新代码；root 消费完整数学回执及最终 success。

固定 $p=47,q=4513,c=5,\delta=5$。
R1072 的 $235$ 个原 coarse 圆盘由其原 consumer 重建，并比对既有
character/coarse-point SHA；仅作为本次新辅助图的输入。
R1074 的八个全局可能标签及已证 first-lift 坐标原样消费：
$$
J=0,\ -3375,\ -12288000,\ 16581375,\ 8000,\ 1728,\ 287496,\ 54000.
$$
原 ID 分别为 $0,76,77,100,108,141,196,220$。
本次未重开 $283$ 筛选、原 $L'$ 证书或已认证 CM first-lift 计算。

## 2. 原全部辅助点的覆盖及独立计数

R1083 先纸证全部标量情形及 special-fiber 重数。
本次程序逐个 $j\in\mathbf F_{4513}$ 求实际 elliptic trace：
一般 $j$ 一个 quadratic representative，$j=0$ 六个 sextic twists，
$j=1728$ 四个 quartic twists。另加入全部 $23$ 个 rational cusps。

实际回执为：

| 项目 | 数量 |
|---|---:|
| 全部 elliptic model 表示 | 4521 |
| 有 fixed necklace 的模型 | 2174 |
| 无 fixed necklace 的模型 | 2347 |
| affine necklace 表示总数 | 7094 |
| cusp 表示 | 23 |
| 一般 $j$ 的真实粗模点 | 4876 |
| $j=0$ 的真实粗模点 | 1 |
| $j=1728$ 的真实粗模点 | 553 |
| 原 $X(\mathbf F_{4513})$ 总点数 | **5453** |

这里 $7094$ 不是原曲线点数。
一般 quadratic twists 仅把 Frobenius 乘 $-1$，其 necklace 作用相同。
特殊点必须用 R1083 的 twisted Burnside 重数；总点数独立于标签像计算。

### 2.1 实际四个 Gaussian twists

primitive finite-field generator 在本次原模型枚举中为 $7$。
四个 $y^2=x^3+Ax$ 模型的回执是：

| $A$ | trace | Frobenius full order | half-order | 固定 necklaces | 不同完整标签 |
|---:|---:|---:|---:|---:|---:|
| 1 | −94 | 4 | 2 | 25 | 25 |
| 7 | −96 | 2 | 1 | 1081 | 553 |
| 49 | 94 | 4 | 2 | 25 | 25 |
| 343 | 96 | 1 | 1 | 1081 | 553 |

四个表示集的标签并集恰有 $553$ 个，与真实粗模纤维点数相同。
两个 scalar 分支都由独立的真 $47$-torsion 基计算；
没有取退化的 $Q=\pi P$。
另两条反射分支、原 effective automorphism 重数均保留。
所有四个模型都保留原 $J=1728$ 的全局标签。

### 2.2 六个 Eisenstein twists

六个 traces 依次为 $50,-83,-133,-50,83,133$；
每个固定一个 necklace，六个 canonical 标签完全相同，
均为原 $J=0$ 标签。
这与独立的 coarse 纤维点数一一致。

其余模型中，判断反射用的是 trace **模 $47$** 为零，
并包含整数 trace 非零的相应分支。
非标量重根没有 fixed necklace；
一般 trace $\pm96$ 未被误当成 scalar。

## 3. 原相位及实际零坐标

全部原 half-point 集有 $1104$ 个元素。
逐真实 Frobenius orbit 求原 $\psi_5$ 的完整乘积，
核 closure、base-field 下降及每个 norm/± 纤维的 $48$ 个半点重数。
scalar 的 half-order 为一，不能用 ambient norm 替代。

实际 Kummer 指数为 $(4513-1)/47=96$。
固定根是 $\zeta_0=2$，原十个 good 角色及圆单位读数为：

| $R$ | 26 | 28 | 30 | 32 | 34 | 36 | 38 | 40 | 42 | 44 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $B_{\omega^R}(\zeta_0)$ | 23 | 10 | 22 | 38 | 40 | **0** | 20 | 46 | 9 | 30 |

原真实 Weil root $\zeta_J$ 与 $\zeta_0$ 的转换逐 necklace 保留
$D_\chi^0=a^{1-R}D_\chi$，同时逐行核相同的圆单位运输公式。
$R=36$ 的零值没有被除去；这一坐标严格要求 $D_{\omega^{36}}^0=0$。
全部角色、同一 coarse 点及同一 cusp $h$ 同时比较。
这正是 R1073 的等式条件，不是逐角色选择不同的辅助点。

## 4. 单射性与同一个 CM 点

程序完整得到 $5453$ 个不同的十角色 canonical 标签。
另一方面，§2 不使用标签的原点数也是 $5453$。
R1073 已保证标签在实际粗模点上良定义，§2 已覆盖全部原点。
所以这个有限映射的像基数等于定义域基数，得到
$$
\boxed{
\mathcal T_{4513}:X(\mathbf F_{4513})\longrightarrow\mathbf F_{47}^{10}
\text{ 单射。}}
\tag{1086.1}
$$

八个旧全局 CM 标签全部存活，而且各自在其真实
$J\bmod4513$ 的纤维中找到匹配。
设 $x\in X(\mathbf Q)$ 是 R1074 的任意候选，
同一唯一全局 cuspidal 标签对应其中一个有理 CM 点 $c_J$。
原全局函数在该辅助素的 specialization 给
$$
\mathcal T_{4513}(\bar x)
 =\mathcal T_{4513}(\overline{c_J}).
$$
由 (1086.1)，
$$
\boxed{\bar x=\overline{c_J}\quad\text{于原 }X(\mathbf F_{4513}).}
\tag{1086.2}
$$
这不仅是相同 $j$，也保同一个原 necklace。
零圆单位坐标不妨碍 (1086.1)–(1086.2)。

合 R1074，原 $x$ 与同一个 $c_J$ 同时具有：

- 原 $47$ 的同一已识别 CM tube，以及原 scaled-$j$ 精度；
- $283$ 的同一原曲线点约化；
- 本篇 $4513$ 的同一原曲线点约化。

这些是下一步同一来源高度计算的输入，不是盘内唯一性的结论。

## 5. 哈希、保留范围与后续输入

| 对象 | SHA-256 |
|---|---|
| 本次 consumer | 758df1a12306555605dde7db91ef2ab6d2aa62d9853dd134a875046e88ebaa7f |
| 本次 method | 883f4e68c13d3394fc1e4a49b9703a97296ad652a40d94de010635500db6a00a |
| 本次 request | 655d3f21b34d6c87f3e7eac95e3b9621c7989e4afc21c625a6b8416fa0dd6493 |
| 已认证原角色输入 | 880799848773da716df2dd4b5db76c07fcc0027e281baff963aff0eeeaf82014 |
| 已认证原 $235$ coarse 输入 | 12025eb9c76692312c856360add6a4702cbe02ccaf51def477bafeaf5e06d1ee |
| 完整排序辅助标签像 | c6933e9806c2c6e83b5b19f22b27962d5b01808dbc4f79d05a3c083805c5f324 |
| 八个已认证标签摘要 | 6a1c2261bd27b3c69d3bf1438ce6e41dd2877bcc41f1c724b656fd4adc701382 |
| runner 完整 payload | a8b402ae734f33aa5b7db6ce17f0b38382836caed4668289848a7f2e3b8643fa |

完整 payload 为 $1796264$ bytes，只留 runner scratch。
未提交或上传可重算 raw 数组、artifact 或 Release。
可复现入口：

- [consumer](../scripts/original_p47_ell4513_cuspidal_transfer.py)；
- [method](../notes/2026-11-27-original-p47-ell4513-cuspidal-transfer-method.md)；
- [request](../notes/original-p47-ell4513-cuspidal-transfer-request.json)；
- [R1083 原覆盖与标量证明](R1083-original-level47-auxiliary-Hecke-fields-and-scalar-fibers.md)；
- [R1073 原全部同点标签](R1073-original-split-auxiliary-cuspidal-sieve.md)。

R1081 的十六个真实一次整 Hecke 块现可在这些相同原约化点上使用。
R1085 给六个 ordinary CM 点的原整 $B_q$ 对数首矩。
其实际块值、原 MW 格、完整高度首项及两个 supersingular CM 点
仍须继续付款。这里没有将有限标签单射或固定 $47$ 进展当作全 $p$ 的完成。
