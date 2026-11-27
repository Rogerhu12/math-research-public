# 原 p47 / ell4513：八个全局 CM 标签的完整辅助同点转移

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

## 新输入及范围

本次固定 $p=47,q=4513,c=5,\delta=5$，执行 R1073 的原完整
同点标签，并纳入 R1083 已证明的全部标量分支。
R1081 已认证 $q$ 上十六个实际一次整 Hecke 块；本次只支付这些块
后续高度工作所需的同点约化输入，不再计算 Hecke 谱或 $L'$。

R1072 的原 235 圆盘向量由钉住的旧 consumer 重建并严格比对
角色及 coarse-point SHA-256；它只是新任务的输入。
R1074 真实 run45928658257/job140275928914 已把全局可能性缩为八个
有明确原 $j,\mathrm{twist},t$ 坐标的 CM 标签。
请求只取这八个已认证 ID 为待转移标签，不重开旧 $283$ 筛选，
也不把旧 227 个排除重报为本次结论。
八个 CM first-lift 已在 R1074 认证，本次消费其坐标，不重复该新源计算。

## 全部原模型、标量与真实粗模点数

枚举全部 $j\in\mathbf F_q$。
一般 $j$ 用一个 quadratic representative；另一个 quadratic twist
只把 Frobenius 乘以 $-1$，对原 necklaces 的作用相同。
$j=0$ 保全部六个 sextic twists，$j=1728$ 保全部四个 quartic twists。
逐模型 exact character sum 给 Frobenius trace，并检查 Hasse 范围。

R1083 已证明：标量 mod $47$ 只可能在 $j=1728$，其中
trace $\pm96$ 是 $\pm I$，每个固定全部 $1081$ necklaces；
trace $\pm94$ 是 projective 非分裂对合，各固定 $25$。
一般 trace $\pm96$ 的 conductor-$47$ CM 模型是非标量重根，
没有 fixed necklace，不把相同 trace 当成标量判据。
其余模型仅在 characteristic polynomial 不可约时有贡献；
trace 模 $47$ 为零时固定 $25$，其它不可约情形固定一条。
这里判断的是 trace mod $47$，不能只测试整数 trace 等于零。

六个 $j=0$ traces 应为 $\pm50,\pm83,\pm133$，每个固定一条。
原 twisted Burnside 独立给 coarse 纤维点数
$$
\#j^{-1}(0)(\mathbf F_q)=1,\qquad
\#j^{-1}(1728)(\mathbf F_q)=553.
$$
全部 $23$ cusps 有理。一般纤维的上述固定数加上 $1+553+23$
给独立的原曲线点数，绝不以模型或 necklace 表示数替代。

## 真 torsion 基和所有原 necklaces

非标量不可约分支沿原方法取 $P,Q_0=\pi P$。
按完整 Frobenius 阶构造有限域，实际群阶先除去全部 $47$ 部分，
再从非零 Sylow 点逐次乘 $47$ 找到真阶 $47$ 的点。
核 characteristic equation、原 Miller Weil pairing 及
$e(P,2Q_0)=e(P,Q_0)^2$。

标量分支不能取 $Q_0=\pi P$。
trace $96$ 在 $\mathbf F_q$、trace $-96$ 在 $\mathbf F_{q^2}$
确定性搜索两个真阶 $47$ 的点；第二个必须不在第一个的完整
$47$ 点 cyclic subgroup 中。另核两点的 Frobenius 均为相应
$\pm1$ 倍和真实 Weil pairing 的非平凡性。

以原 $\delta=5$ 枚举全部
$$
J=\begin{pmatrix}a&b\\d&-a\end{pmatrix},\qquad
a^2+bd=5,\qquad J\sim-J,\qquad AJA^{-1}=\pm J.
$$
完整计数分别为 scalar 的 $1081$、反射的 $25$ 或一般的一条。
实际 Cartan 基是 $(P,JP)$，原 root 是 $\zeta_J=\zeta_{\rm nat}^{d}$。

## 完整原函数、norm 重数、相位与零坐标

全部 $1104$ 个非零半点按真实矩阵 $A$ 的 Frobenius half-orbit 分组。
每条 orbit 从真 $\psi_5$ 评价及逐次 Frobenius 计算实际乘积；
标量 $\pm I$ 的 half-orbits 长度为一。
必须用实际 half-order，不能用 ambient extension norm。

对每个 $J$ 用
$v_1=w/d,v_0=u-av_1$ 按 $[v_0^2-5v_1^2]\in\mathbf F_{47}^\times/\pm$
分组；核每条 orbit 标签恒定、每组 $48$ 个半点和总数 $1104$。
全部乘积必须真正落在 $\mathbf F_q^\times$。

Kummer 指数准确为 $(q-1)/47=96$。
全部 circular-unit 读数也在新 $q$ 重新计算。
按 R1073 的 $a^{1-R}$ 将同一个点所有角色同步运输到固定
$\zeta_0$；逐点核 circular-unit 的相同运输身份。
若某个 $B_\chi=0$，仍比较 $C_\chi B_\chi=D_\chi$，不除以零。

最后加入原全部 $23$ 个 cusp 行，同一行所有角色必须取同一个 $h$；
实际求所需 $B_{\chi^2}$，即使该平方角色不在原 $V$ 内。

## 同点转移验收

每个已知 CM 标签都必须在其实际 $J\bmod q$ 纤维中找到匹配。
六个 $j=0$ twists 的共同标签应一致。
另记录全部 $j=1728$ 真实标签像，数量不能超过 $553$。

完整标签像已覆盖全部原 $\mathbf F_q$ 点。
只有当其基数等于上面的独立粗模点数，才声明全点标签图单射；
结合 R1074 唯一全局 CM 标签，这时原有理点在 $q$ 必须约化到
同一 CM 点。若像较小，只登记完整像与碰撞，不声称同点转移成功。
无论哪种结果，都不由此声称原 $47$ 圆盘内部唯一性或 Serre 完成。

## 预算、来源与可复现性

只在本公开仓库 Actions 运行一个 job。总数学预算 $600$ 秒，
预留 $30$ 秒；workflow 的 $15$ 分钟是安装与调度外限。
python-flint 固定为 $0.9.0$，全部算术为 exact integer/finite-field。
先核 Actions 仓库、实际 HEAD/GITHUB_SHA、请求 SHA、两 README
和全部源码/数学来源 SHA，再开始计时并导入算术。

仅提交脚本、方法与参数；完整 torsion、orbits、模型/tag 数组只在
runner scratch。stdout 只记小摘要、特殊纤维、进度、run/source/hash
和预算回执；不上传 artifact、Release 或可重算 raw。
失败只给准确完成范围与错误，不对未完成图作数学排除。

原来源：R1071、R1072、R1073、R1074、R1083。
原整块用途：R1081。root 与 global_route 已全文逐行纸审新代码及方法；标量基、完整半轨道、独立粗点数与全图注入验收均核通过。
