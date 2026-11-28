# 首次输入：正 e、k 首值 4、lambda 极点的三个完整原局部式

日期：2026-11-29（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127，GPT-6 Astra Pro（AI-assisted）。

这是一个尚未执行的新输入。只计算一个此前未展开的更深原中心；不续接旧六射线初始理想，不重算其纯权公因式，也不改任何冻结输入的预算或算法。

## 1. 明确原中心

已刊[正 e 原估值限制](../results/R150-appendix-unit211-W-b0-positive-e-ray-original-lambda-valuation-and-two-pole-centers.md)证明：在 $v(e)>0,v(k)=0$、$\bar k\ne-2$ 上，lambda 非零且 $v(\lambda)\le0$；若它有极点，只有 $\bar k=4$。本次只针对后者，全部 $\bar k=-2$ 和单位 lambda 情形继续保留。

定义实际局部坐标
$$
E=e,\qquad Y=k-4,\qquad X=(2\lambda-3)^{-1}.
$$
三者均为正赋值；$Y=0$ 可以原样取值，不要求它非零或倒它。反恢复为 $k=4+Y,\lambda=(X^{-1}+3)/2$。原 $X\ne0$ 只来自所研究的极点支；未把其它谱支删除。

## 2. 唯一原输入与尺度

从已刊源 blob 47281af16fdd0ad7500ecda377c3cb9f9d65e725 的必要定义，重新生成同一点的完整 $q_2,R_6,N_5$。其源 SHA256 为 e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8。仅取原定义，没有旧规范化、投影、cofactor 或伪除法尾段。

固定三个新的局部有理式
$$
F_q=\frac{q_2X^2}{Q},\qquad
F_R=R_6X^6,\qquad F_N=N_5X^5.
$$
这里 $N_5$ 保完整原 NV 的已刊来源，不施加物理 $f=0$；$b_0$ 用原 $\kappa$ 恢复，不新增 D 或几何头逆。

在 $\mathbb Q[E,Y,X]$ 上逐式检查约分后分母在原点非零并且是 $1009$ 单位，输出完整四阶 Taylor 多项式 $J_i$。准确返回
$$
\operatorname{num}(F_i)-\operatorname{den}(F_i)J_i
\in(E,Y,X)^5.
$$
实际日志会保每个原分子、分母、jet、完整余式的 profile/SHA，以及最多35项的完整四阶公式。文件只存源码、此输入和后续小回执；不另存大系数载荷或分片缓存。各系数在 $1009$ 的整性也逐式记录。

这只是完整局部原关系，不自动给所有有理估值的最低项或局部空性。没有预设 jet 的常数项、最低次数或任何消去结果；只有实际返回后才可据完整公式继续纸面估值推导。特别高于四阶的余项必须保有明确估值界，不能把截断式当完整原方程。

## 3. 固定执行身份与边界

- 自包含源码：2026-11-28-unit211-W-positive-e-k-four-pole-three-original-local-jets-8542.py。
- 源码 SHA256：eb5463c4638bfa434add15bb7d2c3258353bee86fdc4a5bef569af3c67c1a147。
- 精确运行环境：Python 3.12.14、python-flint 0.9.0，单线程。
- 首次固定预算：120 秒、1 GiB；外驱动135秒，仅允许回收日志。
- 无源依赖缓存，无新 gcd、resultant、Gröbner、局部单位搜索或无穷序列循环。
- 此次未执行，不预报成功、profile、原空性或完成范围。若资源边界到达，如实记录返回部分并冻结同一目标，不加时或换算法续跑。

数学运行前实际部分克隆并 pull，检查根和本题 README 的差异；任何新规则先执行。完整公开图与普通 Hilbert ISP 尚未完成。
