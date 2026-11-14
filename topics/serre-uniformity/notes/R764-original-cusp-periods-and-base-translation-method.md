# R764 预运行方法：原尖点周期、三个平移及完整 Hom 格的基点泛函

日期：2026-11-14。版本：v2 重构；执行环境不可用后，依据完整数学记录及远端 R738/R754/R759 的实际源代码字段重新写成。不是原 scratch 的逐字恢复版。

**本方法没有实际数值结论。** 只有 R754 和 R759 均完整成功，且 request 填入它们真实 run、source、artifact、manifest 和逐文件 SHA 后，才能运行本任务。初始 request 是 pending 模板；现正式 request 已绑定成功的 R754 run 43620862489（source b36d2c58b39f42a694236d48f64444bb6fe1d0af）及 R759 run 43625474728（source 4728e6868e2509556e5c60e138fd97c9b4120d8e）。这只确认两份实际输入已就绪，尚不声称 R764 的尖点标签或基点余数计算成功。新算术只在公开 Rogerhu12/math-research-public 的 Actions 执行。

## 1. 复用的准确对象

原源 $X_1$、$c_0$、$c_1$、原正目标 $C/L:y^2=x^3+b$ 及微分 $dx/(2y)$，全部保持 R735/R738/R745/R751 的规范。固定 $p=41$、$K=\mathbf Q(\zeta)$、$\operatorname{Im}\zeta>0$、$L=K(b)$ 的同一个次数 7 模型。$c_1=4424$，$g_*=(15130,123;123,1)$，$c_0$ 的原标签是 $[2876,2822,2823]$。

R762 已证明原 deck $\delta$ 恰固定 20 个尖点和 $c_0$，商亏格为 127；每个实际正向整数周期映射 $f_0$ 满足 $f_0(c_0)=O$ 和 $f_0\delta=[\zeta]f_0$。以参考 cusp $P$ 平移为零的 $f_P=f_0-f_0(P)$ 仍等变，其在全部固定点上的值只可能是
$$
T_0=O,\quad T_1=(0,-b_{1/2}),\quad T_2=(0,+b_{1/2}),
\qquad b_{1/2}=-U^{20}S(U)^3/8.
\tag{764.1}
$$
这是 R735/R751 原实方向的符号。程序不重算 $U$、$S$、$b$ 或目标挠点；它只在已认证的七次 $b$ 域里做线性合成。

## 2. 输入与完整生产者边界

固定旧输入：

| 来源 | 文件 | SHA-256 |
|---|---|---|
| R735 run 43608152850 | p41-original-CM-model-certificate.json | 752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574 |
| R738 run 43612108090 | original-cosets-and-markings.json.gz | 6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161 |
| 同一 R738 | integral-compact-Manin-cycles.json.gz | d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf |

正式 request 已按上述两次真实成功运行及完整 manifest SHA 绑定：

- R754 小证书 p41-original-period-and-Hom-kernel-certificate.json；
- 同次 R754 的 R754-original-relative-periods.json.gz；
- R759 小证书 p41-original-integral-period-lattice-and-degree-certificate.json；
- 同次 R759 的 R759-original-integral-maps-and-bounded-recovery-input.json.gz。

wrapper 核每个生产者完整 manifest 的指定 SHA，核 manifest 中各文件的 SHA，再核 run receipt 的 complete、source commit、run id。核心逐一核证书中的 stage SHA 和 configuration。R759 configuration 内的 R754_certificate_sha256 必须恰等于本次读取的同一个 R754 小证书 SHA；不允许把两次不同周期计算混接。

实际 core SHA 另由 request 明确给出。R754 要求完整 800 闭链验证、真实约束秩 36、核维数 6；这些是生产者成功条件，不是本任务在其未返回前宣布的数值。R759 必须给出真实全整数格秩 12、同一目标、原 c0 基点、全部正次数及 12 个原微分向量。R764 不重新生成旧拓扑、有限表示、周期、Hom 核、整数格或次数。

## 3. 第一步：原 19 条树边的精确合成

R738 的 dual_tree_edges 是已保存的 19 条边，不在本任务重新选树。每条边保存正负陪集 $(g,gS)$，原方向严格是
$$
\operatorname{cusp}(gS)\longrightarrow\operatorname{cusp}(g).
\tag{764.2}
$$
20 个 cusp 的编号和轨道直接读 R738；根是包含 coset 0 的原尖点。每条树边都必须属于原 819 条 relative_basis_edges。

R754 保存的原周期为
$$
\Pi_{e,j}=\frac{R_C}{\Omega_0}\int_{g0}^{g\infty}\omega_j\in L.
\tag{764.3}
$$
准确 normalization 字符串、原 $6^{-1}$ 相位和不二次施加 $c_1$ 相位的标志均核对。R759 的第 $i$ 个实际映射微分是
$$
h_i=\sum_{j=0}^5v_{i,j}\omega_j.
$$
本任务只新算
$$
\lambda_{e,i}=\sum_{j=0}^5v_{i,j}\Pi_{e,j}.
\tag{764.4}
$$
因为两端都是等变固定点，$\lambda_{e,i}$ 必须属于
$(1-\zeta)^{-1}\mathbf Z[\zeta]\subset K$。程序先在真实 $L=K(b)$ 里相乘，随后严格检查所有非恒定 $b$ 系数都为零，才能取其常数坐标。没有浮点投影或有理重构。

七次域元素用 $a(b)+c(b)\zeta$ 表示，二者均次数小于 7；输入分母完整保留。乘法是
$$
(a+c\zeta)(d+e\zeta)
=(ad-ce)+(ae+cd-ce)\zeta,
\tag{764.5}
$$
按原 R735 单首七次多项式约化。只需要乘加，没有大域逆、280 维运算或新 torsion 枚举。

每完成一条边即原子写入 R764-nineteen-original-tree-edge-periods.json.gz，保 12 个映射的精确 $K$ 坐标。中断后只续未做的边；完整阶段直接复用，configuration 必须一致。

## 4. 第二步：原树路径、尖点标签和基点平移

沿既有树作遍历，得到各尖点 $C$ 从 $P$ 出发的唯一有符号路径。保留边号和正负号，用 (764.4) 相加得到
$$
\lambda_{C,i}=a_{C,i}+c_{C,i}\zeta.
$$
必须准确满足
$$
(1-\zeta)\lambda_{C,i}
=(a_{C,i}+c_{C,i})+(2c_{C,i}-a_{C,i})\zeta\in\mathbf Z[\zeta].
\tag{764.6}
$$
令两个整数坐标之和模 3 为 $\nu_i(C)$，即
$$
\nu_i(C)=
(a_{C,i}+c_{C,i})+(2c_{C,i}-a_{C,i})\pmod3.
\tag{764.7}
$$
标签对应 (764.1) 的准确正负。R762 的推导使用
$\Omega_0/(1-\zeta)=2P_3+\zeta P_3\mapsto(0,+i)$ 及
$R_C^3=i b_{1/2}$，所以 $\nu=1$ 是负 $b_{1/2}$，不能改成正号。

对于实际次数 $d_i$，数
$$
n_{i,\nu}=\#\{C:\nu_i(C)=\nu\}.
$$
R762 的固定点局部次数 $e\equiv1\pmod3$ 与非固定轨道贡献 $3e$ 给
$$
d_i-n_{i,\nu}\equiv
[\,f_{P,i}(c_0)=T_\nu\,]\pmod3.
\tag{764.8}
$$
程序要求三个余数恰为 $[1,0,0]$ 的排列；唯一 1 给出
$\nu_{0,i}$ 和 $f_{P,i}(c_0)=T_{\nu_{0,i}}$。原 based map 为
$$
f_{0,i}=f_{P,i}-T_{\nu_{0,i}},
\qquad f_{0,i}(P)=-T_{\nu_{0,i}}.
\tag{764.9}
$$
失败时不任选平移。这个步骤完全不需要另求 CM 端点积分或实际 RR 函数。

## 5. 全格、$\zeta$ 作用与下一函数恢复数据

对 R759 的全部 12 个整数格基映射都执行以上过程，不只选择最短的一个。以 $P$ 为基点的映射相加仍以 $P$ 为基点，且 $c_0$ 的像在同一个三阶群内。因此
$$
(\nu_{0,0},\ldots,\nu_{0,11})\in\mathbf F_3^{12}
$$
是整个真实整数 Hom 格上的平移线性泛函。

R759 的 $\zeta$ 矩阵按**列**记录 $\zeta h_j=\sum_iJ_{ij}h_i$。
因 $\zeta$ 在 $\ker(1-\zeta)$ 上平凡，每个 cusp 标签行及 c0 标签行必须满足
$$
\nu J=\nu\pmod3.
\tag{764.10}
$$
这项检查直接使用已保存矩阵，不重新求整数格或次数形式。

每个实际 $d_i$ 还附上 R762 的确定商 RR 参数
$$
m_i=\left\lceil\frac{d_i+127}{820}\right\rceil,\quad
M_i=820m_i+d_i,
$$
基展开至 $q_Y^{M_i+d_i}$，原 $h_i/dQ$ 展开至 $Q^{3M_i+4d_i}$。
这些只是由真实次数派生的后继任务输入；程序不声称原商函数或 $\beta$ 已生成。

## 6. 输出、失败保留和续算

完整大阶段仅入 artifact：

1. R764-nineteen-original-tree-edge-periods.json.gz；
2. R764-all-original-cusp-labels-and-c0-translations.json.gz。

第二份保留全部 20 条原树路径、所有精确周期与整坐标、240 个 cusp 标签、12 组计数和唯一 c0 标签、完整平移泛函、实际选定映射及商 RR 界。

小证书 p41-original-cusp-periods-and-base-translation-certificate.json 保留全部生产者 SHA、20/19/12 计数、12 个真实次数和标签、原分支、全部有限恒等式标志及两阶段 SHA。它明确 actual_rational_functions_beta_or_height_computed=false。小 receipt/manifest/source/方法入 Git；可重建的坐标状态只保 artifact。

固定 Python 3.12、python-flint 0.9.0；核心检查版本并在公开 guard 后解除大十进制整数的字符串解析上限。算术完全精确，没有工作精度参数。核心预算 15 分钟；若停止，wrapper 保留所有已写阶段、源/README SHA、stderr/stdout 和失败 receipt，后继 request 以完整 manifest 续算。完整阶段和最终证书直接复用，只有未完成边执行新乘法。

wrapper 复用 p41_public_actions_recovery 的 publish/read/save/sha；发布器保留既有 README 变化检查与非快进 pull --rebase 循环。workflow 只监听正式 request.json，pending 模板不触发。

## 7. 何时才允许登记结果

必须同时具备：

- 完整且同源绑定的 R754/R759 真实产物；
- 每条新树周期严格落 $K$，每个 $(1-\zeta)$ 倍周期严格整；
- 每个映射的三个次数纤维余数唯一指定一个 c0 标签；
- 全 12 映射与 20 cusp 的 $\zeta$ 作用恒等式通过；
- complete 小证书及全部阶段 SHA。

本预运行方法只给算法及证明。成功后登记的也只是实际 cusp/base 平移与后继 RR 输入；真正 $q/\beta$ 坐标、Poincare 规范和高度仍须继续计算。

依据：[R762](../results/R762-original-mu3-quotient-and-single-function-map-recovery.md)、原 R735/R738/R745/R751 结果、R754 及 R759 已公开方法与源码。
