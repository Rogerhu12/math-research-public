# 真正58：已付反射射线上的共同α/R2原盒任务

日期：2026-11-16。**新科学任务的明确范围；本文件和源码编写不构成执行结果。**

本任务落实[R525](../results/R525-one-parameter-common-R1-R2-curvature-fibers-and-polynomial-original-box-domain.md)。原[反射方向观察](true58-reflected-R1-ray-selected-fiber-infeasible-no-candidate-20261116.md)已经闭账：共同BVLS成功，首选α=3/8的唯一新R2 LP status2，无向量/对偶、0预测/actual。当前仍58，祖先累计 **2882.412483226秒 /147 full values**。旧剩余时间、旧LS和旧LP全部保持关闭。

新问题在一条已经实际得到的射线上，同时选择共同幅度与二阶补偿，不对离散幅度挨个重解原LP。它是局部非线性求解；失败不能成为整射线、全51维或主机制的准确排除。

## 1. 固定输入及原始身份

当前58 physical为 **94950b2bd5d7b5241e14333a4315b073f64840f74849a7909d6de8cb3cc29f54**，ind168为 **e2d52f849596a5e7bbf596b66d7805587acc944c1549c5648ee4e115548ed2bf**。固定g、b0、永久reference、原172盒、新九坐标、原14门及容差全部保原身份。

读取四个已完成research stdout，每个只读取一次：

| 原用途 | run / research job | 使用范围 |
|---|---|---|
| 原实际58 | 43859882465 /133273598120 | COMPLETE、CACHE2、FINAL_CLOCK；当前168、原池/门、U/T/e/f及selected metric |
| 永久constructor | 43832870561 /133182173190 | 原55 COMPLETE仅提供未改的reference/原高度坐标构造；不把55当当前点 |
| 已闭纯R2环 | 43865295208 /133292183126 | MODEL、COMPLETE、FINAL_CLOCK；原完整环二jets/G及精确嵌入 |
| 已闭反射R1 | 43873254906 /133319615177 | MODEL、COMPLETE、FINAL_CLOCK；原xstar、V17/Vx/Zx/Lx/Hxx和末成本 |

各raw字节、SHA、JSON加LF身份和源码提交完整写在本次request。新反射MODEL原13,312,899 B，SHA256 **ca0aec1d95949c467042eb74b94314a4490d6742e5cf76f040eeba060d1b8f3e**，不是选读报告的重新序列化。

原ring半径a直接从58 CACHE2的selected_current168_geometry中，按metric_radial_ids的原id141取metric_a，保所选grid/原数组hash/原selected binding。两网都保存时须保同一binary64值；两网均没有这个id则如实报告输入缺失，不从Xt范数推断、不重新评价旧metric或几何补齐。

只存Hxstarxstar，未存任意R1的完整二次张量。下一模型沿这个原xstar，不能暗中重新拟合或扩大为自由x17。

## 2. 同一原盒中的19变量

物理变量为 $(\alpha,y_{17},h)$：

$
q_{\rm ideal}=q_{58}+\alpha E_1x_*+E_2y,
\qquad
c_{\rm ideal}=c_{58}+\alpha P_1x_*+P_2y.
$

$\alpha\in[1/64,1/2]$，原51个末切向坐标可变，其余121个物理坐标保持。完整172盒和
$h\ge4\|\alpha P_1x_*+P_2y\|_\infty$
逐项保留，目标min h。h最大值由原盒足量导出，不另加旧1/128。

数值后端可用同一问题的固定可逆坐标 $(\alpha,z_{17},h)$：
$y_j=s_jz_j$，其中
$s_j=1/(4\max_\ell|W_{\ell2}|)$
仅由原精确R2物理列固定。保存原尺度、后端raw19与解码物理19，两者分别命名；不把解码向量冒称原OptimizeResult.x。约束行的正尺度也在起点固定并保存，求解中不随候选改变。

唯一初点α=1/4。按该α的准确原剩余R2区间取各坐标中点，再构造完整物理norm的h；准确中点在原盒内；缩放解码后的binary64初点须保自己的准确盒判定，不先声称它或初点曲率可行。零宽坐标和原常数门完整保，不能除零或造自由度。

## 3. 完整有限曲率域

每网使用同一α和y：

$
U=U_0+\alpha V,\quad
Z_{12}=C_0+\alpha Z,\quad
Z_{11}=B_0+\alpha L+\alpha^2H+V_{17}y,\quad Z_{22}=D_0.
$

所有原向量都包含完整角Π及中段支持，模型阶段不重新生成frame、Π、168几何J或ordinary。新代数系数、点积和解析导数确属新科学执行，全部计费。

令 $E=U\cdot U,F=U\cdot T$，保原实际G，不强置G=1。
$w=U\times T,Q_{\rm cross}=w\cdot w$；原Schur量为
$q_\perp^2=E-F^2/G$。其浮点运算路径不同，保实测差而不假定逐位相等。

原环metric预算ε=.26600541463999305，两条二次门为
$\varepsilon(1+\varepsilon-E)-F^2\ge0$、
$\varepsilon(E-1+\varepsilon)-F^2\ge0$。
这是原58的环候选域，不是最终.26或主1e−6门。

按R525，以正分母的a,b,c,t,R分子完整保三条谱门：
$4K^2G^2Q^3-t^2\ge0$，
$R\ge0$，
$R^2-K^2G^2Qt^2\ge0$，
其中 $K=1000/61$。对α次数至多6、4、8；R非负不能因平方而删掉。原metric在G≥ε时给数学冗余下界Q≥G(1−ε)>0；若将该下界用于浮点闭域，记录其确切实现，不冒作连续误差认证。

后端返回之后必须另读原单位、未平方的完整PSD/trace/determinant行及原直接metric。不得以缩放后或平方后的微小残差代替原门，不能把单独不可变列门当完整曲率。

## 4. 唯一会话及完整用量

| 项目 | 范围 |
|---|---|
| 总科学范围 | 600秒；输入/导入/源码读取/新代数/求解/输出同一时钟 |
| 新模型构造 | 1 |
| 非线性求解会话 | 1，SLSQP，解析Jac；不重启、不增额、不内嵌旧LP |
| solver子时钟 | 120秒；在回调处检查，非抢占底层调用，实际超额如实保 |
| maxiter /完整新评价 | 160 /至多400 |
| 相同输入重复回调 | 读取同一已付缓存，不重复科学收缩；保attempt/cache-hit与真正评价数 |
| 旧科学复跑 | 0 BVLS、0固定α LP、0输入ordinary/几何J/frame/Π |
| 合格候选后的预测准备 | 至多1次新固定g数组、2次已付首jet绑定，明确计费 |
| 完整候选预测 | 至多1；原同两网、完整metric+curvature |
| actual | 至多1pair/2full values，沿原actual14与准确172盒 |
| 原源账户 | 2882.412483226秒/147值，原封闭账保留 |

预测准备延后到新求解返回合格候选之后。若无候选，不为失败任务额外重建固定metric或绑定全grid first jets。预测本身必要的真实新场/二jets/Π计算属于该新预测费用；“模型阶段0旧Π重算”不表示全body预测免费。

成功与失败均保存原raw19、OptimizeResult的全部实际字段、初始化、变量/行尺度、原单位残差、真实迭代/回调记录、最后已完成评价与失败部分。异常中没有真实backend返回时，保异常及真实最后评价，不伪造OptimizeResult或对偶向量。

## 5. 准确合成后才验收

把后端α及已解码y的实际binary64解释为准确有理数，与原xstar和E1/E2准确相加，随后每个受影响168坐标只舍入一次。保未舍入理想点、理想172、rounded168/172和舍入差；中间R1态既不接受也不先舍入。

只有原圈未平方门、直接metric与准确原盒合格，才能进入唯一全body非线性预测。预测要求原完整曲率门通过，且相对当前58的η严格下降至少1e−7；再付原actualpair。原actual14、原池顺序及学习容量保持，不用预测替代实际，不凭某个圈的改善记59。

只要任一阶段没有合格候选，就保真实结果和费用，转下一确实不同的数学问题；不得写成全射线准确不可行。即使接受59，主课题的全时、全域、连续精化和非局部reach仍须支付。

## 6. 输出与规则同步

新workflow与report均先实际pull public和private，核对已读根/题README。出现变化只读diff、执行新规并在HANDOFF记SHA；private只发表规则blob/QUEUE会话状态，不发表正文。源代码及参数绑定后按原source提交执行，私有规则凭据在科学进程前移除。

完整数组和求解payload仅在原Actions stdout/临时runner中；不上传artifact、Release、Git数据或跨run cache。Git只保存源码、参数、原运行身份和人读结论。report以stdlib只读一次已完成research stdout，完整保NONLINEAR_RESULT的原返回和FINAL_CLOCK，observer秒数与科学账分开。最终科学钟在大输出之后采样；stdout自身失败则如实欠回执，不安装替代成功记录。

request、源码和设计推送后由本公开仓库自己的Actions执行。当前设计不宣告任何新数值结果、候选或主完成。


### 后端接口来源

已核对[官方SciPy1.17.0 SLSQP文档](https://docs.scipy.org/doc/scipy-1.17.0/reference/optimize.minimize-slsqp.html)：ftol是后端多项停止判据的阈值；实际返回的multipliers属于内部QP近似，bounds乘子不在其中。保存所有真实返回字段，并保各原行的顺序与固定尺度；这些乘子不自动构成当前非线性问题或整射线的严格不可行证书。
