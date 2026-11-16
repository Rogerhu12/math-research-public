# 原矩阵族的35维迹配对与完整奇点排除入口

作者：Astra-ISP-789f / normal_annihilator；与 /root 联合推导。AI-assisted: GPT-6 Astra Pro。2026-11-16。

**状态：可执行源码已冻结，尚未执行新的数学门。** 本入口不读取已经失效的旧大数组，也不以参数点采样替代完整多项式来源。当前共享执行器离线，首个 Actions 运行承担实际 Python 解析和算术验证。

## 1. 目标及原对象

固定原数域
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$
及已付四个对称 mean 矩阵和它们的原规范矩阵族
$$
A(\mu)=\sum_{i=0}^3\mu_iT'_i,\qquad
M(y)=[T'_0y,T'_1y,T'_2y,T'_3y].
$$
全部变量仍为原自由参数。本次只有固定系数 place $127,d=100$；它不是一次 $y,w,u,\mu$ 点特化。

第一门构造
$$
E[\mu_1,\mu_2,\mu_3]/I_5(A(1,\mu_1,\mu_2,\mu_3))
$$
在已付35个普通单项式基上的三张乘法矩阵和完整迹配对。如果实际迹行列式模127非零，则该原代数在特征零为 étale，几何 rank4 支撑恰35个互异点。它尚不说明这些点都是六次面的普通节点；后者还需要相应的局部论证。

第二门保全部
$$
q_i(y)=y^{\mathsf T}T'_iy\quad(0\le i<4)
$$
及 $M(y)$ 的全部15个4阶子式。按次数5至8建立完整齐次 Macaulay 矩阵。一旦某级全输出行秩满，原 $E$ 系数单位的伴随给
$$
(y_0,\ldots,y_5)^D\subset (q_0,q_1,q_2,q_3,I_4(M)).
\tag{1}
$$
该式排除六次面的所有 rank5 奇点。没有任何一级的不足秩会被升格成特征零非成员或存在性结论。

即使两门均通过，原 Bell=1 的全部剩余临界关系仍然保留，不宣称原理想已经为单位理想。

## 2. 无历史数组的同原张量重建

沿用已实际核验的原完整物理 helper 和当前 Bell 原模型生成器。它们重新建立同一个 $K,J_3,R_3$、全部17个原梯度以及原 Bell 多项式；先核两边 $J_3$ 逆、原 $N/\Gamma$ 梯度身份、全部加权 Euler 恒等式和完整原系数的127合法性。

原 Bell 为
$$
B_r=\beta(y)+y^{\mathsf T}MH,\quad
P=(2,1,0,3,4,5),\quad U=(6,7,8,9,10).
$$
固定原坐标变换可写为
$$
H=Lw+Nu-\tfrac13L\nabla_y\beta.
\tag{2}
$$
这里 $L_U=0,L_P=M_P^{-1}$，而
$$
N_U=I_5,\qquad N_P=-M_P^{-1}M_U.
$$
程序重新核全部 Bell 常单位的双逆和 $MN=0$；所有逆仅为固定系数域元素。

令 $Q_m(u)$ 是原 $\partial_{H_m}R_3$ 在 $H=Nu$ 后的完整 $u^2$ 部分，$Y_{ij}(u)$ 是原 $\partial_{y_i}R_3$ 在同代入后的 $y_ju^2$ 系数。它们只需要原势函数的 $H^3$ 与 $y^2H^2$ 部分，其原来源标签始终保留。四个保留单项式固定为
$$
v=(u_1u_4,u_2u_3,u_2u_4,u_3u_4).
$$
在其余11个二次单项式上，取全部11个原 $Q_m$ 的系数方块 $U_{11}$。只在本次真正核得 $\det U_{11}\not\equiv0\pmod{127}$ 后，使用
$$
\widehat Y=Y-Y_{\rm elim}U_{11}^{-1}Q.
\tag{3}
$$
程序核全部396个被消坐标和540个完整二次来源乘回。

**(3)逐项给出此前的同一组四个 $E$ 矩阵，不仅给出有限域中碰巧相同的数值。** 以下论证在 $E$ 上进行。

由完整原坐标逆，11×11常矩阵 $[L,N]$ 可逆。新六个 $w$ 梯度和五个 $u$ 梯度的二次首项为
$$
\begin{pmatrix}L^{\mathsf T}\\N^{\mathsf T}\end{pmatrix}Q.
\tag{4}
$$
它们因此与全部11个原 $Q_m$ 张成同一二次空间。新 mean 梯度为
$$
\partial_{y_i}R'
 =(\partial_{y_i}R_3)\circ(2)
   +\sum_m\frac{\partial H_m}{\partial y_i}
       (\partial_{H_m}R_3)\circ(2).
$$
其 $u^2$ 部分严格等于 $\sum_j y_jY_{ij}(u)$ 加线性 $y$ 倍的 $Q_m$。$w$ 与纯 $y$ 平移均不改变这些最高二次系数。

旧算法先消5个平方，再消6个指定混合项；新算法按(3)一次消同一11维空间。两者都只在同一组四个 $v$ 上取余项，且被消11坐标方块为单位，所以该余项唯一。固定每个 mean 行、每个 $y_j$ 和每个 $v_l$ 后，其 $E$ 系数必逐项相同，即同一 $T_l$。这证明同原性，不依靠任意有限域行列式或直线匹配。

代码另核原四个行列式的既有127读数 $(106,93,100,92)$、全部对称坐标，并采用原位置
$$
(0,0),(0,1),(0,2),(0,3)
$$
的4阶单位进行相同规范化。全144个坐标乘回原张量，完整六次式在既有直线上的七个系数也核对。因为原 $T_l$ 和原4个位置均相同，新规范 $T'_l$ 及 $\mu_0=1$ 图也相同。这些数值门只是追加审计。

本次不声称重新展开了旧的巨大 $E$ 张量系数。其真 $E$ 定义是原多项式、(2)、(3)、(4)和固定常数逆组成的精确表达式。所有实际选定常数逆在本次 place 均有非零剩余，因此这些表达式也定义在下述原整系数环上。

## 3. 真正的同原 $D$-自由35基

令 $D$ 为原系数域在 $127,d=100$ 处的离散赋值环。由于原三次式的首项模127为42、该根的导数为49，原首一模型在此处 étale。上述所有原常数单位均在 $D$ 中可逆。

对称矩阵的21个原上三角余因子记为 $c_i$，在 $\mu_0=1$ 后写为
$$
c_i=\sum_{|\alpha|=5}C_{\alpha i}\mu^\alpha+\ell_i,\qquad
\deg\ell_i\le4.
$$
程序重新构造全部余因子和整个21×21系数矩阵 $C$，要求同原模127行列式为103，并核其两边逆。于是
$$
\mu^\alpha-\rho_\alpha
 =\sum_i(C^{-1})_{i\alpha}c_i,\qquad \deg\rho_\alpha\le4
\tag{5}
$$
是原 $D$ 多项式身份。反复降总次数给真满射
$$
D^{35}\longrightarrow D[\mu_1,\mu_2,\mu_3]/(c_i).
\tag{6}
$$
[已付原完整自由35证明](../results/R150-appendix-original-corank-two-pencil-exception-algebra-has-free-rank-thirty-five.md)给(6)张量 $E$ 后的维数恰35。其核是 $D^{35}$ 的子模，故无扭；核张量 $E$ 为零便迫核为零。因此(6)本身就是同35基的同构，不先假设平坦性。

程序在剩余域中由(5)构造三张35×35乘法矩阵，核：

- 全21条原余因子的完整 border 来源；
- 三对乘法矩阵的3675个交换坐标；
- 全35个原单项式作用到单位的1225个基坐标；
- 全21个原余因子的25725个完整算子坐标；
- 完整35×35迹配对及其行列式；非零时再核完整双逆。

这些算子是(6)原乘法的剩余，而不是任意构造的35维表示。若迹行列式非零，它在 $D$ 中为单位，原有限自由代数为有限 étale；特别地其 $E$ 纤维几何约化、恰35点。若迹行列式为零，本入口只保存完整实际结果，不报特征零非约化。

## 4. 完整四二次式加十五子式的原来源门

采用(1)的19个原生成元，没有选择参数点或只取独立行。对 $D=5,\ldots,8$，原列为：

- 每个 $q_i$ 乘全部次数 $D-2$ 的六变量单项式；
- 每个原4阶子式乘全部次数 $D-4$ 的六变量单项式。

输出为全部次数 $D$ 的六变量单项式。源字典、全部输出字典和完整系数矩阵 SHA 均保存。

| 次数 $D$ | 完整输出行数 | 全部原来源列数 |
|---|---:|---:|
| 5 | 252 | 314 |
| 6 | 462 | 819 |
| 7 | 792 | 1848 |
| 8 | 1287 | 3738 |

采用 python-flint0.9 的实际 nmod_mat.rref() 接口（返回完整 RREF 与 rank），提取原主元列。只有 rank 等于全部输出行数时，才对相同原列方块计算、核验完整双逆；其非零模127行列式使原 $E$ 方块可逆。以该原方块的伴随回填(1)，不把模127解本身称作 $E$ 解。来源只除固定系数域常数。

在 rank5 的六次面点，原伴随为非零常数乘 $yy^{\mathsf T}$，其中 $y$ 为核向量。因此
$$
\partial_{\mu_i}\det A=c\,y^{\mathsf T}T'_iy=cq_i(y).
$$
同时 $M(y)\mu=0$，所以 $I_4(M)(y)=0$。若(1)成立，就不可能存在这样的非零 $y$ 同时使全部偏导为零。这个论证覆盖完整原 rank5 轨迹，而非若干测试点。

API依据为 [python-flint0.9 nmod_mat 文档](https://python-flint.readthedocs.io/en/latest/nmod_mat.html)。原模型的唯一性与全部有理来源仍由以上公式承担。

## 5. 冻结文件及准确参数

| 文件 | 完整 blob | 字节 | SHA256 |
|---|---|---:|---|
| 主源码 notes/2026-11-16-r150-original-pencil-trace-and-complete-singularity-gates-789f.py | 9c0575db323f24cd278429d4cd787e48b642d062 | 26614 | 4d0fd8ddaa51725b60705813555502036fed310979542aeb2cac8b320b57d326 |
| inputs notes/2026-11-16-r150-original-pencil-trace-and-complete-singularity-inputs-789f.json | 63f9908ceeb91e834563a7cf6008f49de956f815 | 3741 | a7193fe13f0a1c5b0a8e31a3104cfe4f129d1f98550728b3eca2e71762eb4524 |

另外两件原源码的全部 blob、SHA 与字节数在 inputs 中。本入口只导入原 Bell driver 的 prepare()，不运行 Singular，不需要任何历史数学数组。

~~~text
python notes/2026-11-16-r150-original-pencil-trace-and-complete-singularity-gates-789f.py
  --helper {scripts}/2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py
  --field-driver {scripts}/2026-11-16-r150-original-full-bell-homogeneous-source-prefix-789f.py
  --out {work}/original-pencil-trace-and-complete-singularity-gates
  --through complete --through-degree 8
  --seconds 180 --memory-mib 768
~~~

建议外墙240秒。through=prepare 只做同原重建，through=trace 再做完整35代数；默认继续完整齐次门。每个完整 phase 原子保存 gzip、逻辑 SHA 与语义 binding，续接只读已成 phase，不重做它们。预算75仅保存此前完整 phase；单次 RREF 中途状态没有被称为可恢复。实际若需要，可在同源码、同 out 提高秒数至900并继续。

仅 TimeoutError 返回75；MemoryError、原输入与验证错误均返回 failed1，仍保此前完整 phase，不以加秒数自动重试内存失败。完整诊断同时写入 parameters.error={type,message}。全部模型、原系数矩阵、来源逆和临时回执只留 job 临时目录与日志；仓库仅保存源、参数、执行身份与 SHA。无新的判空结论在运行前被预填。
