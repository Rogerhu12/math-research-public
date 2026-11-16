# R865：原 T₇ 的共享短逆消费者执行方法

日期：2026-11-16。状态：工程契约；新 T₇ 矩阵和谱均待公开 Actions 实际输出。

数学来源是 [R865](../results/R865-original-Hecke-T7-from-certified-level82-Fourier-rows.md)。原 R864 基已经实际完成；R866 的同基 Fourier 矩阵、选行和准确逆必须从真实成功产物读取。本方法不另起第二份共同前缀、RREF 或求逆任务。

## 1. 唯一尺度与三个来源组

三个逻辑组为 `R786`、`R864`、`R866`，每组保原 run/source/core/configuration、完整原 manifest 和所选文件 bytes/SHA。R786 的146条原权二行与 R864 的完整原基可以从 R866 活跃载体恢复，不重下已到期祖先，不重算旧数学。原载体全部成员流式核完后，只保这两个仍被消费的组；R866 的完整 source inventory/receipt 继续证明其余已成引理的历史来源。

旧 R786 的原行结构没有独立顶层 `result`；它在 `configuration` 中保原 result/source。仅这个已冻结 producer 接受该实际结构，不能给它改写新字段。新 R864/R866 stages 保完整各自原 result/configuration。任何新输出都用 R865 新 tag。

R786 系数已是 $e_i=82^2T_{1,i}$ 的整数展开；原 `integer_scale=6724` 不指示本程序再乘除一次。R864 矩阵 $B$ 已将 $\sigma=e_1+e_{73}$ 的原 V1 转换做完，本程序直接读其 `original_V1_coefficients`。R866 的 $H=AB$ 是原 $F_j$ 展开，而非微分的全部常数82；$\omega_j=82F_jdq_Y/q_Y$ 的共同82在作用矩阵中抵消。

所消费的 R866 完成项为 `holomorphic_Fourier_matrix`、`selected_exact_inverse`、后者的 `source_row_selection`、`semilinear_action`、`Q_fixed_holomorphic_basis` 及 source audit/stage inventory。$H$ 的560行按 $40n+r$ 排列，$J$ 使用完整560行编号。准确逆 $U=H_J^{-1}$ 的两乘回已由原 producer 完成；此处只读身份与该已成证书，不再执行旧逆乘积。

## 2. 只形成真正缺少的 Fourier 线性组合

目标恒等式是
$$
[q_Y^n]T_7F_j=\Pi_6([q_Y^{7n}]F_j)
 +7\mathbf1_{7\mid n}\Pi_7([q_Y^{n/7}]F_j),\qquad1\le n\le13.
\tag{865M.1}
$$
若所需 $F_j$ 系数的阶在0至13内，直接取已成 $H$ 的对应40行。特别首目标的 $n=7$ 输入和第七目标的 $n=1$ 修正都读取旧块。其余只新增
$$
14,21,28,35,42,49,56,63,70,77,84,91
$$
十二个40×127的 $A_nB$，每个保存独立原子阶段。这里 $A_n$ 本身是读取旧整数行，新的算术只是它对原127基的线性组合。接着保存十三个完整40坐标 T₇ 目标块，q⁰行由原全纯性为零。

两 $\Pi$ 按 $\xi^{40}=-\sum_{r=0}^{39}\xi^r$ 准确约化。它们作用于原 cyclotomic 坐标，固定原 $s$；不作用于已换成 $v=\xi^{-10}q_Y$ 的另一套数据，不改变相位，也不用任何有限域嵌入替代40坐标。

## 3. 原 K 基和真实 Q 固定基的两个矩阵

每次处理8列，读旧 $U$ 求
$$
M_{7,*J'}=U K_{J,J'},
\qquad H M_{7,*J'}=K_{*,J'}.
\tag{865M.2}
$$
第二式在全部560行验证，完成后才保存此坐标块。十三阶全局注入保证它是原全空间的真实 $T_7$，不是一组局部拟合系数。

R866 的真正 $\mathbb Q$ 固定基换基是
$$
P=U D,\qquad D_{kk}=1\ (J_k/40\text{ 的整商为偶数}),
\quad D_{kk}=s^{-1}\ (\text{整商为奇数}).
$$
因 $T_7$ 与原 $c_Y$ 交换，令
$$
N=K_JU
\tag{865M.3}
$$
后，不同所选奇偶的条目准确为零；同奇偶时 $D_{ii}=D_{jj}$。因此
$$
P^{-1}M_7P=D^{-1}ND=N.
\tag{865M.4}
$$
程序按8列保存 (865M.3)，准确核 $M_7U_{*J'}=UN_{*J'}$ 和全部异奇偶零。这样得到原 R866 已认证 $\mathbb Q$ 基上的真实矩阵，不重新求 $P^{-1}$、不重新解下降，也不把原 $K$ 基误称有理基。

## 4. 精确单算子谱与有限对应表达式

按实际所选奇偶拆 $N$ 的两个不变块，分别用 python-flint0.9.0 的 `fmpq_mat.charpoly()` 求特征多项式；每个块单独完成和续接。全部系数必须准确为整数。两个多项式相乘得到完整127次 $\chi_7$，不再第三次对整个127矩阵计算同一特征多项式。

对整多项式使用 `fmpz_poly.factor()`，保存完整不可约因子和重数，并准确乘回 $\chi_7$。不同因子的乘积 $m_7$ 是真正最小多项式，这一点使用 R865 证明的原 Rosati 自伴随性；证书明确标为数学证明的结论，不声称另外执行了127维逐次矩阵幂。

对每个因子 $f_i$ 和补因子 $m_7/f_i$ 求准确多项式 Bézout，验证完整等式和全部因子上的剩余类。CRT 多项式 $E_i$ 满足 $E_i^2=E_i\pmod{m_7}$，各和为1。保存实际分母 $d_i>0$ 与整系数多项式 $d_iE_i$；后者定义由真实循环7对应复合、整数加减得到的有限原对应。没有另物化大投影矩阵或曲线纤维积，不能称这些表达式为已展开方程。

该结果按单个 $T_7$ 分谱，不保证区分全部 Hecke 等型。尤其不计算 modified-diagonal 的各投影值，不给原 $e_\eta$、torsion-clearing $N$、校准主函数、非 $p$ 支持数值或高度。

## 5. 完成边界与恢复

结果名固定 `R865-original-Y-Hecke-T7-and-spectral-projectors`；最终证书名固定 `p41-original-Y-Hecke-T7-certificate.json`。核心 CLI 为 `--config --output --budget-minutes`；配置由标准库 wrapper 从实际来源逐 SHA 展开。新数学只允许 `GITHUB_ACTIONS=true` 且仓库为原公开仓库。

所有数学阶段是根目录 `R865-*.json.gz`。阶段均带同一新 source/tag，写临时文件后原子替换；完成阶段不覆盖、也不重算。manifest 用其实际文件列表的 hash 命名；current 单列并 `complete=false`。失败 FINAL 是历史端点，不用其旧 manifest 引用阻断已经推进的新 current。成功 FINAL 则全部引用必须精确成立。

预算只在新阶段之前检查，允许已经完成的阶段先原子保存；外层 timeout 留出收据、完整 manifest 和上传时间。数学错误、预算停止与完整 scope 成功分别报告，绝不将输入未完成或缺 source 填成数学成功。来源未发布时请求 `producer_inputs_pending=true`、未知 producer 为 null；不得触发。

最终只有完整目标、两个原矩阵、全560×127乘回和全部谱证书都完成时 `complete=true`。旧 Fourier/E1/normal 产品、cusp 核、共享 $H,J,U$ 及原 Q 固定基重算标志均 false。公开上传仅一日 active artifact；Git 只放源码、参数、纸面证明和简明 run/SHA 登记。
