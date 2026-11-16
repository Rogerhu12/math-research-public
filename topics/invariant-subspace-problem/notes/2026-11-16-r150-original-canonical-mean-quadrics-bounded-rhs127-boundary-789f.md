# R150：四个规范均值二次式的完整权八余式

作者：Astra-ISP-789f / literature_audit，与 /root。AI-assisted GPT-6 Astra Pro。日期：2026-11-16。

## 1. 结论与严格范围

在已付原模型的合法剩余点 $\mathbf F_{127}$、$d=100$，令
$$
B=\mathbf F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],
\qquad \operatorname{wt}(y_i)=1,\quad\operatorname{wt}(w_i)=2,
\qquad b=\sum_i y_iw_i.
$$
令 $F=B^{10}$ 保留原十个单项式轴及权 $(0,2,2,2,2,2,4,4,4,4)$。

本次检查的是十九图覆盖中四个字面规范二次式
$$
q_j(y)=y^TT'_jy,\qquad 0\le j\le3,
$$
而不是未作常数变换的原四个 $y^TT_iy$。规范化的完整原身份见 §2。

令 $\mathcal G=B\langle Y,C,V,W\rangle$ 为已付首轮齐次梯度子模：六个原 mean 列 $Y$ 权 $5$，二十个保留低 commutator 列 $C$ 权 $6$，三十个 $V=N_iY_j$ 权 $7$，一百个 $W=N_iC_j$ 权 $8$。十四个旧高列已经有完整原来源落入同一子模；因此原 $17674\times1386$、秩 $1312$ 的完成矩阵给出完整 $\mathcal G_8$。该输入仍保留十四个旧高列及全部原来源标签。

本次实际结果为
$$
q_jb^2e_0\notin\mathcal G_8\qquad(0\le j\le3).
$$
其中 $e_0$ 是原常数轴。四个完整余式的非零坐标数依次为
$$
378,\quad357,\quad378,\quad378.
$$
而且这四个目标的整个四维常数线性空间与 $\mathcal G_8$ 交为零；原增广 $17674\times1390$ 矩阵的秩恰为 $1316$，见 §3。这仍不否定更高权来源或完整原理想的成员性。

相关父结论：

- [规范 pencil 与完整均值 incidence](../results/R150-appendix-original-rank-three-mean-incidence-and-complete-sextic-pencil.md)；
- [四二次式与完整十九图覆盖](../results/R150-appendix-original-mean-quadrics-dual-normalization-and-complete-bell-cover.md)；
- [原高来源换基与三十六低种子稳定闭包](../results/R150-appendix-original-high-source-exchange-and-thirtysix-seed-stable-closure.md)。

## 2. 字面规范化的实际原核验

原模型的四个 $T_i$ 直接由六个原 mean 列的四个 quad 轴提取。本次重新核全部 $24$ 个 mean 坐标和全部 $144$ 个原对称矩阵项。

对 $21$ 个上三角原坐标组成的 $21\times4$ 系数矩阵 $A$，按原精确 pencil 的同一规则取首个独立四行。实际选定的原坐标正是
$$
(0,0),(0,1),(0,2),(0,3).
$$
令 $U$ 为这四行的 $4\times4$ 方阵，$V=U^{-1}$。本次实际 $\det U=74\ne0$，并核全部
$$
UV=VU=I_4,\qquad A'=AV,\qquad A'U=A.
$$
分别对应 $32$ 个逆坐标和 $168$ 个正反 pencil 坐标；选定四行的规范结果严格为 $I_4$。

随后由 $A'$ 重建四个对称 $T'_j$。程序独立以全矩阵公式构造 $y^TT'_jy$，并核
$$
q_j=\sum_i(y^TT_iy)V_{ij},
\qquad
y^TT_iy=\sum_jq_jU_{ji}.
$$
这八个完整多项式恒等式全部通过。采用 ordinary monomial；对角项只出现一次，非对角的两个矩阵项全部保留，没有二分之一重标。四个规范二次式分别有 $18,17,18,18$ 个非零单项式。

该常数变换不引入参数分母，也不以未规范的旧 $T_i$ 代替十九图的 $T'_i$。四个规范多项式及完整矩阵只保存在 TMP 的双哈希阶段中。

## 3. 完整降约和原输入乘回

此次独立新 binding 只读取已经完整结束的原权八状态。全部原状态、字典、输入、结果与 source SHA 在运行前核验；父权七身份也保留，用于原三十个 $N_iY_j$ 来源标签。

四列 $q_jb^2e_0$ 全部展开进原 $17674$ 输出字典。冻结的只读 native 输出每列全部 $1386$ 个原来源系数 $c_j$ 与完整余式 $R_j$，并逐坐标核验
$$
q_jb^2e_0=Xc_j+R_j.
$$
全部 $4\cdot17674=70696$ 个原标量乘积通过，每个余式在原全部 $1312$ 个单位主元坐标处为零，原结果的 EOF、域系数与字典次序均完整核过。运行后全部被消费的父数组 SHA 不变。

完整 native 的 unitCancellations 为零；完整输出逐列确为 $c_j=0$、$R_j=q_jb^2e_0$。根又独立从原 $T_i$、$U,V$ 重建全部四个字面目标，逐全部 $70696$ 坐标核目标等于余式、来源系数全零，以及全部 $1312$ 个原单位子式坐标上的目标均为零。

令 $\rho$ 为这 $1312$ 个原输出坐标的限制。已付原单位子式行列式为 $4\ne0$，故 $\rho|_{\mathcal G_8}$ 单射。另一方面，规范化给四个 $q_j$ 在
$$
y_0^2,\quad y_0y_1,\quad y_0y_2,\quad y_0y_3
$$
四个 monomial 上的系数方阵恰为 $\operatorname{diag}(1,2,2,2)$，其行列式为 $8\ne0$。所以四个 $q_j$ 线性独立。$B$ 是整环且 $b^2\ne0$，乘 $b^2e_0$ 保此独立性。四目标全部被 $\rho$ 杀，因此
$$
\operatorname{span}_{\mathbf F_{127}}\{q_jb^2e_0:0\le j\le3\}\cap\mathcal G_8=0,
\qquad \operatorname{rank}[X\mid q_0b^2e_0,\ldots,q_3b^2e_0]=1316.
$$
这是已付原单位子式与字面目标的直接推论，不是一次新消元。

若某个余式为零，程序还必须恢复其完整十坐标来源，验证原十八生成元的乘积且 Bell 系数为零，再运输到原十七梯度并乘回；最后以
$$
q_j=q_jb^2-(b+1)q_j(b-1)
$$
核全部原十八、原十七加 Bell 乘积和来源权至多 $8$。本次四列均非零，因此没有产生任何这样的正来源证书。

## 4. 来源权不超过 8 的精确含义

这里的来源权约束是：若
$$
qe_0=G+(b-1)H,\qquad G\in\mathcal G,\quad H\in F,
$$
则每个梯度生成列及其系数的总权至多 $8$，并要求 $\operatorname{wt}(H)+3\le8$。不允许引入更高权来源后只因最高项相消就称其来源权至多 $8$。

因为 $\mathcal G$ 的最低权是 $5$，对权 $2$ 的 $q$ 作逐权比较得
$$
H_0=H_1=0,\qquad H_2=-qe_0,\qquad H_3=H_4=0.
$$
权 $5$ 的等式给 $H_5=G_5-bqe_0$；权 $8$ 的等式给
$$
b^2qe_0=G_8+bG_5\in\mathcal G_8.
$$
这里保留了可能非零的中间权 $5$ 梯度项，未错误地要求 $bq\in\mathcal G_5$。反向由 §3 的 Bell 恒等式立即成立。因此
$$
qe_0\text{ 有这种来源权至多 }8\text{ 的表示}
\quad\Longleftrightarrow\quad b^2qe_0\in\mathcal G_8.
$$
实际四个余式非零，分别排除了四个字面规范 $q_j$ 的上述有界表示。

这与此前七个 $\delta$ 右端的非零结果相互独立；没有用旧 $\delta$ 负结果推出本次四列。全部结论限定在原 $\mathbf F_{127}$ 模型与准确来源空间，不作特征零非成员性推论。

## 5. 实际执行和可重现身份

主源码为
[四规范二次式右端消费者](2026-11-16-r150-original-canonical-mean-quadrics-bounded-rhs127-789f.py)，
Git blob 为 26fa7047caaf189d83aa6281d485cf9945d01ae7，
$28292$ 字节，SHA256 为
c3723cdf2b8f6e6f6e3ba0aab45c3d2b2fbb056aedec634df2ccefeded8babe5。

原输入和完整门分别见
[输入清单](2026-11-16-r150-original-canonical-mean-quadrics-bounded-rhs127-inputs-789f.json) 与
[接口](2026-11-16-r150-original-canonical-mean-quadrics-bounded-rhs127-interface-789f.md)。
[完成执行身份](2026-11-16-r150-original-canonical-mean-quadrics-bounded-rhs127-local-execution-789f.json) 保存完整 CLI、原父与源码身份及输出 SHA；数学数组不入仓库。

实际运行于 2026-11-16 15:00:07.701210 UTC 启动，15:00:17.252508 UTC 完成，exit code 为 $0$。数学计时 $9.349584655006765$ 秒，墙钟 $9.551047689994448$ 秒；预算 $180$ 秒、$2048$ MiB，外层 $240$ 秒。父 Python 峰值 RSS 为 $108084$ KiB，子进程峰值为 $195488$ KiB（包括编译）。

数学 binding 为
2e4625501c73ba21bcc5c701212dade8fdc7a9fce19875a9d5a37dc2094a2d79。

完整原回执 $6588$ 字节，SHA256：
1688af057845a567db2a9fa57f3ad6fc7efd129e1634ad1f8b546eae14a0c143。

完整 manifest $8827$ 字节，SHA256：
632c946395b42bf69304492da220c67c0b074beaa4470f57352016d1e66af608。

规范化阶段 $1452$ 压缩字节，物理 SHA256：
ae88e0dcfbe9056630d864c8792e56f822a0a1f31e46c83ecce86d77620a2976；
完整逻辑 $4607$ 字节，SHA256：
35602bb394e7f72251c0459d82acb31a4a29fd21e519049d62be2eb27ab80c7f。

四列完整 native 结果 $76416$ 字节，SHA256：
220708014b8b32121cc9fd1a5e111fa6b77375942757311bdad0c4eba9047584。


## 6. 根的字面原输入独立审计

根使用独立普通 Python 算术，从原模型阶段读取四个 $T_i$，重算 $U,V$、行列式 $74$、全部规范矩阵与四个 $q_j$，没有调用生产者或 native 的函数。随后直接以普通单项式构造四个 $q_jb^2e_0$，逐全部 $70696$ 坐标与原输入和完整余式比较；全部 $1386\times4$ 来源系数严格为零，四个目标在已付 $1312$ 阶原单位子式的全部坐标上严格为零。

因此 §3 的负结论与秩加强可直接由已付原矩阵秩、原单位子式和字面目标推出。此次独立审计实际 exit 0，耗时 2.0080976230092347 秒，峰值 80268 KiB，没有重做消元或写出数学数组。源码见 [原规范目标审计](2026-11-16-r150-original-canonical-q-literal-target-audit-789f.py)，7817 bytes / SHA-256 `bedb8cc28bd8b201d46873cece404f20e8ad517de4e8b4b52107c9785dbc5f08`。完整临时 raw 为 903 bytes / SHA-256 `714fa653d2e9a97d91cb67c488239a7fb23e08ea4d43e2a3a75a51f17686fae5`；[实际执行身份](r150-original-parameter-module-execution-789f/local-20261116-original-canonical-q-literal-target-audit.json)只保存源、参数与输出身份。
