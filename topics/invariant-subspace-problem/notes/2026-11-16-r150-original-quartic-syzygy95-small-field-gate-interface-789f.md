# 原四次来源的 95 维小单位门：冻结接口

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

本入口是新独立源。共享 executor 不可用，故当前仅静态冻结，没有新 AST、编译、rank 或行列式实际。它不引用旧本地未冻结 draft 的执行状态，不预填秩 95。

## 1. 原输入与合法域

同原数域
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$
及已付合法 place $(127,100)$。唯一数学数组输入是完整原 field model 的 base；其 manifest 含全部 116 seeds，并由已审 helper 的 read_paid_base 按完整 stored/logical SHA 验证。

本源只调用该小读取函数，不调用 exact-helper 的 build_constants，不读已中断 exact run 的任何 UI 文件，也不要求新 Q60 求解先完成。它核定全部原十一条二次 top、普通单项式字典和原来源列标签。

记 $q_0,\ldots,q_{10}\in E[u_0,\ldots,u_4]_2$ 为同原十一梯度的二次 top。三个完整矩阵为：

| 矩阵 | 原行 | 原列 | 尺寸 |
| --- | --- | --- | --- |
| $C$ | 全部普通三次单项式 | $u_kq_g$，按 $5g+k$ | $35\times55$ |
| $D$ | 全部普通四次单项式 | $u^\nu q_g$，$|\nu|=2$ | $70\times165$ |
| $T$ | 全部 $q_g$ 二次来源坐标 | $u_\ell z_s$，$s=1,\ldots,20$ | $165\times100$ |

所有单项式均为普通单项式；重复指标不添加多重指标归一或额外因子 2。

## 2. 同原二十个三次 syzygy

按已付原字典重建十一方阵 $U$ 及 inverse、十五个二次正常形来源 $\alpha$ 和四个保留系数 $\rho$。二次保留单项式为
$$
u_1u_4,\quad u_2u_3,\quad u_2u_4,\quad u_3u_4.
$$

原三次单位列恰 $0,\ldots,34$。全部二十个 border 路径 $u_i v$ 合并后有十六个不同三次单项式；其原来源 $X_{i,v}$ 仍保同原五十五坐标，并逐原 $C$ 乘回。对所选二十 low 列 $(0,j,k)$，构造
$$
z_{ij,k}
=u_j\alpha_{ik}-u_i\alpha_{jk}
+\sum_v\rho_{ik,v}X_{j,v}
-\sum_v\rho_{jk,v}X_{i,v}.
$$

必须核 $CZ=0$ 的全部 700 坐标，并核原二十列投影单位非零。所选原 seed IDs 是 $1..5,11..15,21..25,31..35$。这些是原来源，不从某个数值核重新挑选无来源向量。

随后逐项构造 $T_{\ell,s}=u_\ell z_s$，核 $DT=0$ 全部 7000 坐标。原 $D$ 的完整秩 70 是另一硬门。按原 $C$ 满行秩，E 上每个四次单项式也是一次单项式乘原三次来源，故 $D_E$ 满行秩，$\dim_E\ker D_E=165-70=95$。

## 3. 真正未预填的 95 门

只有实际 $\operatorname{rank}_{127}T=95$ 时，才选取原 $T$ 的 95 个列和 95 个行，取得原方阵 $A_{95}$。程序硬核真实非零 determinant，并完整支付两侧 $18050=2\cdot95^2$ 个 inverse 产品。

实际若小于 95，则只输出 completed-diagnostic。有限域退秩不等于 E 退秩；不报告 E 的满射或 high 删除。若 rank 大于 95，则与已核 $DT=0$ 和 rank $D=70$ 矛盾，作为输入/算术硬门失败。

真正的 95 原单位子式使同一个 E 子式非零。这里 E 上的 kernel 恒等不是由有限域零产品上提：原同源恒等严格给
$
D_E(u_\ell z_s)=u_\ell C_Ez_s=0,
\qquad
D_E(u_jX_{i,v}-u_iX_{j,v})
=u_j(u_iv)-u_i(u_jv)=0.
$
其中 $C_Ez_s=0$ 和 $C_EX_{i,v}=u_iv$ 是原二次正常形及原三次来源的多项式恒等。新增 field7000/2800 产品是同源审核，只有 95 子式的非零值用于升秩。

原 $T_E$ 已在 $\ker D_E$，两边维数同 95，因此
$$
E^5\otimes_E\ker C_E \longrightarrow \ker D_E
$$
满射。E 中的系数由这个原 $A_{95,E}$ 的 adjugate 定义，绝不把输出的 F127 数值系数当作 E 系数。

完整 field right kernel 仍另保全部五个自由方向、原 100 来源索引和 825 个乘回坐标。仅其维数可由同原 E 秩推知为 5；这五个 field 向量本身不免费上提。

## 4. 全四十条 high 的原来源门

对每个 $i<j$ 和四个保留二次单项式 $v$，原 high commutator 来源的最高 $u^2$ 部分是
$$
d_{ij,v}=u_jX_{i,v}-u_iX_{j,v}.
$$
程序保全部四十列和原 165 坐标，核 $Dd=0$ 的 2800 个坐标。

若 95 门成，用同原单位行解出 field 系数，再全 165 行乘回全部四十 RHS，支付 6600 个完整坐标。同时原 100 个 $u_\ell z_s$ 对原 95 基列的全部 16500 坐标也重核。这避免只在选行拟合 RHS。

这些 field 数组是实际审核材料。E 上的完整关系由原 kernel 维数和同原 E 单位子式定义，仍不声称本次实际展开了巨大的 E 95 逆或 E high 参数数组。

## 5. 若实际门成功，原完整来源如何下降

此节是明确条件推论，当前不宣称条件已实际成立。

写原 moment 正常形列为 $m=(1,u_0,\ldots,u_4,v_1,\ldots,v_4)$，$N_\ell$ 为已付完整参数矩阵。原 border 来源矩阵满足
$$
m(u_\ell I-N_\ell)=G\Sigma_\ell.
$$
对低列 $c_s$，保实际规范来源 $m c_s=G\sigma_s$，$\sigma_s$ 的最高一次 $u$ 来源为 $z_s$。于是
$$
m(N_\ell c_s)
=G\bigl(u_\ell\sigma_s-\Sigma_\ell c_s\bigr).
$$
第二项的 $u$ 次数至多 1，所以该真实来源的 $u^2$ 顶恰为 $u_\ell z_s$。符号是减号，不能仅在商中写一个未运输的 $N_\ell$ 关系。

用真实 E 的 95 系数从 high 来源中减去这些 $N_\ell c_s$ 来源，最高 $u^2$ 项全消。剩余来源次数至多 1，像仍是十个保留单项式的正常形。因此其最高一次来源位于 $B\otimes_E\ker C_E$；原 canonical-source 唯一性把它精确写回 $C_{20}$，包括原来源向量本身，而不只其商像。得到
$$
C_{\rm high}\subset
B\langle C_{20},\,N_\ell C_{20}\rangle.
$$
全部系数只使用固定 E 常数逆和原参数多项式，无参数分母，原十七梯度来源保持。

## 6. 若成功，至多 270 列的完整 E 呈示

令 $P_0$ 由六 mean、二十 low comm 和十个 Bell 列生成，$P_r=\sum_{|w|\le r}N_wP_0$。上述条件结论使全部 comm 图像位于 $P_1$，low 图像仍位于 $P_0$。

原二次 operator $Q_a$ 满足 $Q_ae_0=0$。对五个一次字面轴，交换误差只用 low comm，故 $Q_ae_{u_i}\in P_0$；对四个二次字面轴，余项是 $N_\ell C_{\rm low}$ 和完整 comm 图像，故 $Q_aF\subset P_1$。没有在此假设 $P_1$ 稳定。

已付原三次降次恒等的词序误差只有
$$
N_\ell Q_aF,\qquad N_\ell C_{\rm full}F,\qquad
C_{\rm full}N_\ell F,
$$
均在 $P_2$。因此长度三的 operator word 可降为长度至多二并加 $P_2$，严格给 $N_\ell P_2\subset P_2$。二字路径再按原十一条二次关系和四个保留路径减少，得到 26 个非 Bell 种子各用 $1+5+4$ 个词，加十个已稳定 Bell 轴：
$$
26(1+5+4)+10=270.
$$

这里是稳定闭包由 36 个种子生成并至多两轮完成，**不是**初始 76 列与 36 列的普通 B 模相等：新列 $N_iC_{20}$ 可能不在初始普通 B 模中。这不是有限域 200/210 压缩的上提；未支付 E 的另一项第一轮压缩。它也不证明 Bell=1 判空。

## 7. 冻结源、参数与执行

| 文件 | Git blob | bytes | SHA256 |
| --- | --- | ---: | --- |
| 2026-11-16-r150-original-quartic-syzygy95-small-field-gate127-789f.py | a472cf1b3d9fd3e45319e0b4b2a9060f1adce9e8 | 15520 | b6f72e376aa403ff540a01927ea0dd4ac136099cb7be16fe201f91e95968cc4c |
| 2026-11-16-r150-original-quartic-syzygy95-small-field-gate-inputs-789f.json | e7ff8a21bd07d67d4be1795dc2bea1b7b7a79345 | 4561 | 0bb74295098553fee18c3b3e1dbff5c404a38c242a339fb877e29ee86182bb3a |

主源只用冻结 v2 helper 的小 reader 和原 field model；所有父 pins 在 inputs 中。官方 [python-flint 0.9.0 nmod_mat 文档](https://python-flint.readthedocs.io/en/latest/nmod_mat.html) 已逐项核对 rank、rref 返回值、inv、transpose 与四参数构造。核心结论仍由全部原乘回门和同原子式支撑。

建议作为同 job 第五步，依赖原 field model 完整成功：
~~~bash
python 2026-11-16-r150-original-quartic-syzygy95-small-field-gate127-789f.py \
  --exact-helper {scripts}/2026-11-16-r150-original-low-commutator-twenty-exact-constants-v2-789f.py \
  --field-model-source {scripts}/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py \
  --field-model-out {work}/original-ten-parameter-module127-v2 \
  --out {work}/original-quartic-syzygy95-small-gate127 \
  --seconds 60 --memory-mib 512
~~~

使用原 observer，outer120 秒，10 秒心跳。本小源要求全新独立输出目录，未实现恢复；75 或失败只保真实已完成文件/身份供审查，不伪称接续。没有批准的自动重试。

两个可能的临时相位是 whole-original-quartic95-input 和 complete-original-quartic95-unit；最终 raw 是 original-quartic95-receipt.json。所有矩阵、profile、raw 只留临时目录，仓库只存本源、参数、证明及真实执行身份/SHA。
