# 原 Padé Hankel 配对的全带宽自伴随算子诊断

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：已完成。** run46071081257 的八个系统均只有标量解；准确结论及全部pins见[R1145](../results/R1145-original-Pade-banded-self-adjoint-exclusion.md)。只对四个固定输入作新的精确诊断。
不重跑 R1134 的十五 Euler 列或既有零点窗口，也不将有限结果推广到一般素数。

## 1. 原对象及这次问题

保持 [R1137 §2](../results/R1137-original-Lame-conjugation-with-complete-boundaries.md)
的原函数
$$
N=(p-5)/6,\qquad
F(x)=\sqrt{1-x}\,G_N(x)=\sum_j f_jx^j,\qquad
G_N(x)={}_2F_1(1,-N;1/2-N;x).
$$
仅使用 $p\in\{101,107,131,137\}$。在所需安全范围 $0\le j\le2N+1$，
R1137 的 $3xF'+F=(1-x)^{-1/2}$ 给
$$
f_j=\frac{(1/2)_j}{(3j+1)j!}
=\frac{2N+1}{2N+1-2j}\frac{(1/2)_j}{j!}.
$$
两式分母在本范围均为单位。脚本另由完整 $G_N$ 与平方根相乘独立形成同一列，
逐项确认，而非把一般 Hankel 矩阵替换成原对象。

令
$$
H_N=(f_{i+j+1})_{0\le i,j<N}.
$$
对每个 $b=1,2$，求出所有满足
$$
T_{a,c}=0\quad(|a-c|>b),\qquad H_NT=T^{\mathsf t}H_N
$$
的 $T\in M_N(\mathbb F_p)$。不先假定带上的系数为行号的某个低次多项式。
这里“commutant”文件名仅指这组配对自伴随方程，不声称 $H_NT=TH_N$。

这样的 $T$ 保持 $\ker H_N$，因为
$H_Nv=0$ 推出 $H_NTv=T^{\mathsf t}H_Nv=0$。标量矩阵总在解空间。
这只是寻找可控制实际 Padé 缺陷的候选算子；存在非标量算子本身仍不排除缺陷。

## 2. 完整线性系统及证书

未知量依字典序列出所有 $T_{a,c}$（$|a-c|\le b$）。对每个 $i<j$，
该未知量在方程中的系数是
$$
\mathbf1_{c=j}(H_N)_{i,a}-\mathbf1_{c=i}(H_N)_{a,j}.
$$
因 $H_N$ 对称，这些正是全部非冗余位置方程；对角自动为零。

每次运行同时给出：

- 确切秩与完整右核维数；恒等矩阵确在核中。
- 核基的独立性与全部方程消去，以及同阶单位子式给出的秩下界。
- 系统矩阵和核基的 SHA-256、所用行列及子式值。
- 若存在非标量解，输出至多三个实际带状矩阵，全部直接核验配对关系。
- 四输入、两带宽全部结束才输出 completed；预算耗尽不会宣称完成。

只有解空间维数恰为一时，才可断言**该输入和该带宽**的解全为标量。
矩阵维数大于一不等于原 $e,K_4$ 已非同时零；某些输入为标量也不排除更大带宽、
边界补偿、一般 $p$ 的其它算子或真正 de Rham 推前。

## 3. 执行与可复现范围

- 脚本：[original_pade_banded_commutant.py](../scripts/original_pade_banded_commutant.py)。
- 参数：[original-pade-banded-commutant-request.json](original-pade-banded-commutant-request.json)。
- workflow：.github/workflows/serre-original-pade-banded-commutant.yml。
- SageMath 10.6 镜像固定于现有公开 workflow 的同一 digest。
- 只允许本公开仓库的 GitHub Actions 执行；读取原脚本和请求为只读挂载，
  不写可重算数据、artifact 或 Release，输出小型摘要与哈希。
- 内部总预算 300 秒，预留 20 秒；外部 360 秒硬截止；4 CPU、14 GiB。
- 每项结果最终只登记 run、结论、脚本/请求/输出哈希；不能在得到日志前登记数值结论。
