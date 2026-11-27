# R1134：四个原单源的低阶低次数 Euler 算子排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，范围为四个指定素数的完整有限精确计算。**
没有给一般素数的阶数下界，也没有证明原 $e,K_4$ 非同时零。

## 1. 准确结论

令 $p\in\{101,107,131,137\}$，保持原 $v^2=-108$、
$p=6k-1$、$N=k-1$、$m=(p-1)/2$、相对 Cartier/Fourier 规范。
写
$$
\Phi(U^m)=U H(U^3),\qquad
\widetilde H(z)=H(-v^2z),\qquad
\Theta=z\,d/dz .
$$
则在 $\overline{\mathbf F}_p$ 上不存在非零算子
$$
\boxed{
L=\sum_{j=0}^{d}z^j P_j(\Theta),\qquad
d\le2,\quad \deg P_j\le4,\qquad L\widetilde H=0 .
}
\tag{1134.1}
$$
这里 $P_j$ 的系数为常数。若允许任意有理系数或更高次数，
本定理没有作相应排除。

## 2. 原源与完整矩阵

[原 Lamé 续稿 (T31)](../notes/2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)
给准确有限生成
$$
\Phi(U^m)=\delta^{-1}\sum_{s=0}^N c_s\delta^{-6s}D^{6s}U,
\qquad
c_s=[t^{6s+1}]U(t)^{-1/2}.
$$
程序在同一个 $\mathbf F_p[U]$ 中使用
$D^2=4(U^3+v^2)\partial_U^2+6U^2\partial_U$；
$c_s$ 由 $y''=3v^2y^5$ 的有限递推得到。
所有用到的 $6s(6s+1)$ 分母都低于 $p$。

每个原输入均通过三项验收：$D^{p-1}U$ 与原 binomial 公式的
$\delta$ 相同且非零；完整纯极分解重构恰为 $U^m$；
[R1061.85–86](R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)
的独立完整配对 $C$ 恰为 $-1$。
从未除未知的 $h_0$ 或 $h_N$ 来归一化。

写 $\widetilde H=\sum\widetilde h_n z^n$。
最大算子类的十五列按 $(j,i)$、$0\le j\le2$、$0\le i\le4$
排列，完整系数矩阵为
$$
M_{n;(j,i)}=(n-j)^i\widetilde h_{n-j},
\qquad 0\le n\le N+2.
\tag{1134.2}
$$
越界系数为零；零次幂为一。
所有最高次方程均保留，故 $L\widetilde H=0$ 当且仅当对应列向量在右核中。

精确结果如下；所列 minor 始终取第 $0,1,\ldots,14$ 行与全部十五列。

| $p$ | 原 $\deg\widetilde H$ | 完整矩阵尺寸 | 秩 | 指定 minor 的行列式模 $p$ |
|---:|---:|---:|---:|---:|
| 101 | 16 | $19\times15$ | 15 | 36 |
| 107 | 17 | $20\times15$ | 15 | 30 |
| 131 | 21 | $24\times15$ | 15 | 63 |
| 137 | 22 | $25\times15$ | 15 | 7 |

四个行列式均非零，所以完整右核为零。
常数域扩张保持这十五列的线性无关，故结论也在代数闭包成立。
较小 $r,d$ 的列集合是同一最大矩阵的子集，全部一起排除。
这证明 (1134.1)。

## 3. 真实执行与可复建来源

- 源代码：[original_single_source_euler.py](../scripts/original_single_source_euler.py)。
- 有限请求：[original-single-source-euler-request.json](../notes/original-single-source-euler-request.json)。
- 方法与边界：[有限诊断方法](../notes/2026-11-28-original-single-source-euler-diagnostic.md)。
- source commit：f360fd32cdd94b4ecda54df701e5cee95ce07745。
- [公开 Actions run 46050577346](https://github.com/Rogerhu12/math-research-public/actions/runs/46050577346)，
  job 140680567162；真实状态 success，SageMath 10.6。
- 实际数学运行约 2.896051466 秒，预算 300 秒、预留 20 秒。
- source SHA-256：1804a4aa134629bdc9e763b98392fffdb925828b8d59d93c20bad64b6d9d0325。
- request SHA-256：52dcfa3a2d2f699c6f5f30fe3384bc439a8457bc4f30b8331e5453a5ad34a9dc。
- 完整小结论 canonical certificate SHA-256：
  9a88755aa14f68a314d551f84efff633a6d5d1b8dd40e67aeaa4e0df90fd1398。

root 直接读取原 job 日志，确认三个来源验收、四个完整矩阵及成功收尾，
并用文本元数据重核 source/request/canonical certificate 的哈希。
全部系数、矩阵、秩及行列式只在本公开 Actions 计算；
未本地执行数学，也未保存可重算数据、artifact 或 Release。

## 4. 后继范围

此结果排除四个实际输入上的指定 Euler 类。
它说明不能未经证明给原指定输出套上该类 Gauss/Heun 小阶方程。
它不排除更高阶、更多奇点、较大系数次数或其它有界秩系统；
也不把这四个素数外推为所有充分大素数。
继续从完整原核的高 $\Psi$ 插入与实际 Hermite 余核取得下一项输入。
