# R1145：四个原 Padé 配对的全部三、五对角自伴随解均为标量

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，范围为八个指定有限线性系统的精确计算。**
不是一般素数定理，不证明原 $e,K_4$ 非同时零。

## 1. 原对象与准确结论

保持 [R1137 §2](R1137-original-Lame-conjugation-with-complete-boundaries.md)
的原函数与原相对 Cartier 来源：
$$
p\in\{101,107,131,137\},\quad N=(p-5)/6,\quad
F(x)=\sqrt{1-x}\,G_N(x)=\sum_{j\ge0}f_jx^j.
$$
所需系数为
$$
f_j=\frac{(1/2)_j}{(3j+1)j!},\qquad
G_N={}_2F_1(1,-N;1/2-N;x),\qquad
H_N=(f_{i+j+1})_{0\le i,j<N}.
$$
所有被使用的 $j\le2N+1$，分母均为模 $p$ 单位。
对 $b=1,2$，令
$$
\mathscr T_b=
\{T\in M_N(\mathbb F_p):T_{a,c}=0\ (|a-c|>b),\
H_NT=T^{\mathsf t}H_N\}.
$$
则在上述每一个输入上，
$$
\boxed{\mathscr T_1=\mathscr T_2=\mathbb F_p I_N.}
$$

尤其，此处完全不限制非零带上的系数随行号如何变化，
并非只排除某种低次多项式的参数化。
任何此类配对自伴随算子都会保持 $\ker H_N$；
本结论表示在这些输入上没有可供使用的非标量三、五对角算子。

## 2. 与原系数的一致性

R1137 的原方程 $3xF'+F=(1-x)^{-1/2}$ 给上述 $f_j$。
在本特征中 $2N+1=-2/3$，故亦有
$$
f_j=\frac{2N+1}{2N+1-2j}\frac{(1/2)_j}{j!}.
$$
脚本不只使用这个递推：它独立形成完整 $G_N$ 的系数
$$
g_0=1,\qquad
g_j=g_{j-1}\frac{j-N-1}{j-N-\frac12}
\quad(1\le j\le N)
$$
以及 $\sqrt{1-x}$ 的系数，再卷积至 $2N+1$，
逐项核实两种定义相等。
这里 $5/6=-N$、$4/3=1/2-N$，所以保留原 R1137 函数，
未替换为另一个具有相似参数的超几何函数。

## 3. 完整系统与秩证书

按字典序以 $|a-c|\le b$ 的全部位置为未知量，
以 $i<j$ 的全部位置为方程。
系统矩阵 $A_{p,b}$ 的相应条目恰为
$$
(A_{p,b})_{(i,j),(a,c)}
=
\mathbf1_{c=j}(H_N)_{i,a}
-\mathbf1_{c=i}(H_N)_{a,j}.
$$
这正是 $H_NT-T^{\mathsf t}H_N$ 的全部独立位置；
因 $H_N$ 对称，对角条目恒为零，另一半是其负。
因此 $\ker A_{p,b}$ 与 $\mathscr T_b$ 完全相同。

实际运行得到：

| $p$ | $N$ | $b$ | 方程数 | 未知量数 | 秩 | 核维数 | 同阶子式模 $p$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 101 | 16 | 1 | 120 | 46 | 45 | 1 | 76 |
| 101 | 16 | 2 | 120 | 74 | 73 | 1 | 59 |
| 107 | 17 | 1 | 136 | 49 | 48 | 1 | 18 |
| 107 | 17 | 2 | 136 | 79 | 78 | 1 | 68 |
| 131 | 21 | 1 | 210 | 61 | 60 | 1 | 109 |
| 131 | 21 | 2 | 210 | 99 | 98 | 1 | 44 |
| 137 | 22 | 1 | 231 | 64 | 63 | 1 | 51 |
| 137 | 22 | 2 | 231 | 104 | 103 | 1 | 23 |

脚本给出并核验完整右核基、其独立性、全部系统方程及表中非零子式。
实际八个子式均取各自矩阵的前“秩”行和前“秩”列；索引自零开始。
恒等矩阵在每个系统的核中，故秩至多为“未知量数减一”。
表中的同阶非零子式给出相反不等式，核恰一维，
且非零恒等矩阵生成它。这完成有限结论的证明。

## 4. 真实运行、参数与哈希

- 公开 Actions [run 46071081257](https://github.com/Rogerhu12/math-research-public/actions/runs/46071081257)，attempt 1。
- job 140747905385，全部步骤 success；计算输出 completed=true。
- 源提交：9fbde3f799dabd74c223d7afaaf3cfc7f625dacb。
- SageMath 10.6，镜像 digest
  60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879。
- 脚本：[original_pade_banded_commutant.py](../scripts/original_pade_banded_commutant.py)。
- 参数：[original-pade-banded-commutant-request.json](../notes/original-pade-banded-commutant-request.json)。
- 请求方法：[诊断说明](../notes/2026-11-28-original-Pade-banded-commutant-diagnostic.md)。
- 脚本 SHA-256：
  cd6abecb693db72f01091208f272dee5a9e206f86aa7c61330d7f5de1a266ab4。
- 请求 SHA-256：
  ee7af9b5f650caf3c3edf4de165795b2e497c5bd0240e296e703b3fb182da3f2。
- 最终 canonical JSON 输出 SHA-256：
  7d3dc7ab85f9ac191e55221878810daf68b1bbadebe6c255f45c03acbf2b3d65。
- 脚本记录总耗时 3.847 秒。root 只读取真实日志并核 provenance/hash，
  没有在本地或 V8 运行数学程序。

按根 README 第15条不保存可重算矩阵、核基、日志副本或 artifact。
上述脚本、参数、运行和哈希足以定位及重现全部系统和证书。

## 5. 保留的范围

本结论仅排除八个系统内的非标量算子。
不能推出所有 $p$ 都只有标量，不能排除更大带宽、带边界修正的关系、
另一个真实推前上的连接，亦不能以此代替原 Padé 缺陷的排除。
某个一般公式在这四个输入上退化成标量，也不与本结论矛盾。

此计算与 R1134 的原 $\Phi(U^m)$ Euler 系统不同。
R1134 及旧零点窗口不再重算。现继续 R1137 的实际双缺陷、
带第三类补偿的 proper de Rham 推前以及原算术杯积端点。
