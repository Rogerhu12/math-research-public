# 固定曲率目标 70 的可行短步：实现与实际入口

本稿仅定义一次新的数值恢复策略。既有完整度量、不可变高度基、163 维物理表示、原参数盒以及全部几何门保持不变。真实几何计算仍只能在本公开仓库的 Actions 中执行。本地开发检查只使用显式人工模型和纯数组线性问题。

## 1. 改动来自已保存的实际证据

来源是公开 run `43648433010`，source `df535c0c42d76040903b1e89c6d08d13ea360ad2`，其完整报告为：

`notes/actions-43648433010-1-curvature_feasible_exchange/curvature-feasible-exchange-audit.json.gz`

decoded SHA256 为 `87945a59c206618ca2da5fe0b31f8a5961c1bef085704aa5bf27494c7daecf32`。

随后只读提炼 run `43651096112` 的 120 个 trial 和 73 个 callback，没有重新评价曲面。唯一满足全部既有物理门的保存态仍是

`e407a21488257097f60073f7e46e19f987dc963760957040ee7254a02889beb4`。

该态两档角网格的最大曲率约为 $73.35984304$ 与 $73.35982955$。细网格实际度量误差为 $0.2671465317390794$，距既定上界 $167/625=0.2672$ 仅约 $5.35\times10^{-5}$。内条带也只有很小正裕量。

第 6 次 trial 的曲率约 $56.0035$，但度量误差 $0.2677719160$ 已超门，且该 trial 没有保存完整系数。它不能作为新初值。最后的已保存非初始 trial 曲率约 $208.20$、度量误差约 $3.027$，并非可接受恢复点。继续压低辅助 $\lambda$ 曾使池内不可行持续、遗漏行大幅增长，因此本次从 e407 重新开始，固定目标 $\lambda_\star=70$，不重放旧优化，也不续用失败 trial。

本次仍固定完整度量

`fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6`。

$\lambda_\star=70$ 只是一个小幅曲率改善目标，不是已取得的界，也不是 reach 设计目标 $1/\tau=1000/61$。

## 2. 目标与不放松的几何门

沿用 [R103](../results/R103-actual-metric-curvature-semidefinite-gates.md) 的真实第一、第二基本形式及四个缩放 PSD 行。若 $I$ 是实际第一基本形式、$II$ 是实际第二基本形式、$q>0$，则

$$
q(\lambda_\star I+II)\succeq0,\qquad
q(\lambda_\star I-II)\succeq0
$$

给出曲率上界的必要且充分局部代数条件。实现保留既有 trace/determinant 缩放和所有解析参数导数；没有把目标度量代替实际 $I$。

下列条件仍按旧定义、旧数值容差独立检查：

- 真实直接度量误差 $\eta\le167/625$；
- 完整原参数盒及共同帽高的仿射门；
- 所选上半带的 signed-$z$ 门；
- 球半径 $101/100$ 与内条带 $|y|\le0.38999$；
- $\tau=61/1000$ 的镜像点对门及独立正则筛。

这些是采样门，不是连续证书。镜像门也没有覆盖所有点对。即使取得 $\kappa_{\max}\le70$，仍远未支付目标 $1/\tau$，更未取得整面 reach 或准确等距。

## 3. 只在已接纳物理态处建立线性模型

令 $p$ 为当前已接纳的 163 维物理系数，$d$ 为试探改变量。当前 active pool 完整继承第十二份报告的索引，既有行不删除。每个模型只在已通过两档角网格的物理态处建立；失败 trial 不成为下一线性化点。

写当前池内物理行值为 $c_i(p)$，原容差为 $\epsilon_i$，解析导数为 $J_i$。本次线性模型约束为

$$
J_i d\ge-\frac12\bigl(c_i(p)+\epsilon_i\bigr).
$$

这保留当前已知裕量的一半，仅是线性预测。真实候选依旧必须按原门重构检查。没有把真实门容差放宽为 LP 容差。

固定目标曲率行写为 $k_j(p;\lambda_\star)$。仅这些行允许一个非负模型松弛量 $\rho$：

$$
k_j(p;\lambda_\star)+D_pk_j\,d+\rho\ge0,\qquad \rho\ge0.
$$

原帽高行与参数盒不加松弛。$\rho$ 是 LP 的模型变量，不是曲面参数或可接受曲率证书。$\lambda_\star$ 固定，LP 中没有降低它的变量。

设原盒为 $\ell\le p\le u$，初始信赖比例为 $\vartheta=1/100$。对有宽度的坐标取

$$
s_j=\vartheta(u_j-\ell_j),\qquad d_j=s_j y_j,\qquad |y_j|\le1,
$$

同时保留原盒。零宽度坐标固定。加入 $t\ge|y_j|$ 后，LP 目标为

$$
\min\ \rho+10^{-6}t.
$$

使用 SciPy 的 `linprog(method='highs')`，所有变量边界显式提供。LP 返回后独立检查其矩阵行和盒残差；失败不会触发真实几何试探。LP 容差、线性模型残差限和每次时间限都在新评价身份中记录。这不是全局或局部可行性的证明。

## 4. 每一步的两网实际验收

对一个 LP 步，按 $1,1/2,\ldots,1/32$ 依次回溯，最多六次。每个候选先在原完整径向网与 384 个角节点上重构全部普通二 jets。

只有粗网物理门全部通过，且其真实曲率可能取得至少 $10^{-3}$ 的改善或达到 70 时，才进行同参数的 768 角纯值复核。细网不请求 Jacobian。接纳须同时满足：

$$
\begin{aligned}
&\text{384 与 768 网格的原物理门均通过},\\
&K_{\rm new}<K_{\rm old},\\
&K_{\rm old}-K_{\rm new}\ge10^{-3}
\quad\text{或}\quad K_{\rm new}\le70+\epsilon_\kappa,
\end{aligned}
$$

其中 $K$ 是两网真实最大绝对主曲率的较大者。原曲率数值容差 $\epsilon_\kappa$ 不变。

因此，只有池可行、只有 384 可行、或只有辅助 PSD 行下降都不够。若 768 失败，旧已接纳态仍是下一轮物理初值；该失败候选连同完整系数、两网门值保存。

所有已评价 trial 都用于在 384 全网收集遗漏的违反行，按原容差补回池，包括最后退出时观察到的行。失败 trial 可以提供约束信息，但不提供新的物理初值。768 在本轮只作验收网；没有假装它的角节点已进入粗网 Jacobian 池。若细网门持续阻止短步，这将是有明确记录的新限制。

全部回溯失败时信赖比例减半。若 LP 没有模型改善、达到最小信赖比例、池容量上限或任一共享预算，保留最后两网已接纳态并退出。不重启无限次，不把无进展当无解。

## 5. 预算、计时与内存

本轮最多：

- 12 个线性模型；
- 40 次初始化及试探的完整普通几何值评价，384 和 768 调用共同计数；
- 120 秒优化活动时间；
- 每模型最多六个回溯点；
- 每个 LP 最多 10 秒，且不超过剩余活动预算。

初始两网和第一次分批 Jacobian 预构建单列初始化耗时；最外层入口记录十二输入 loader、准备、优化、末复核以及完整 process 总壁时。末尾同状态的两个独立值复核另列两次调用和耗时，不包含第二次求解。

复用既有“16 个 owned 径向行加 $0,L$”的二 jet Jacobian 分批。没有形成 $160\times384\times163$ 的全约束 Jacobian。约四千池行时，LP 稠密矩阵约为 $4300\times165\times8$ 字节，约 5.7 MB；原几何分批的瞬时数组仍可能占主要内存，不能把小 LP 矩阵误报为完整 RSS。新增细网 cache 是普通值，不含参数 Jacobian。报告沿用实际 RSS、最大 batch、普通 jet 一致性和各类 Jacobian 字节账。

## 6. 输入、物理身份与保存

新 driver 先调用已有严格十一输入 loader，再完整绑定第十二份报告的源、run、字节 SHA、初末态、完整 $g/b_0$、实际节点及行池。第十二份报告必须仍选择原 e407，且其两档角网门通过。

新报告把旧失败 metric $\delta$、旧曲率 $\lambda$ 及旧预算退出保留为历史，不重新规范为成功。新固定 70、LP 松弛与信赖比例只属于本次求解/评价定义，不进入物理 state。

保存三类彼此分开的内容：

1. 所有粗、细普通值 trial 的完整 binary64 有理系数、物理 SHA 和门值；
2. 每个 LP 模型、预测步、回溯、遗漏行补回及退出原因；
3. 单调接纳的两网物理状态序列。

父类中已有的“仅粗网 best”仍可保留作诊断，但新最终选择只取第三类。任意错误、细网失败或预算退出都不把最后未通过 trial 当作可 warm 的结果。最终 freeze 核完整系数、$g$、$b_0$ 和物理身份不变，再对同参数重算 384/768；若复核失败，报告明确失败，不自动重新优化。

紧凑 summary 保留科学门、时间、计数、模型与 trial 的小标量，以及完整报告 SHA；大系数向量、整个 canonical 模型、径向明细保存在完整报告中。发布压缩只是存储处理，不改科学数据。

## 7. 新文件与运行接口

新源仅两件，不修改已发布库：

- `scripts/frame_curvature_feasible_steps.py`
- `scripts/frame_curvature_feasible_steps_audit.py`

开发入口：

~~~bash
python scripts/frame_curvature_feasible_steps_audit.py \
  --check-only --out "$RUNNER_TEMP/curvature-feasible-steps-development.json"
~~~

真实入口沿用上一报告的全部十一组路径及 decoded SHA 参数，新增：

~~~text
--feasible-curvature-audit notes/actions-43648433010-1-curvature_feasible_exchange/curvature-feasible-exchange-audit.json.gz
--expected-feasible-curvature-sha256 87945a59c206618ca2da5fe0b31f8a5961c1bef085704aa5bf27494c7daecf32
--out $RUNNER_TEMP/curvature-feasible-steps-audit.json
~~~

真实入口必须为 `GITHUB_ACTIONS=true`、仓库准确为 `Rogerhu12/math-research-public`，且输入位于本题公开 notes。本地没有构造或评价 e407 曲面。开发检查覆盖可达固定目标、细网阻挡、真实曲率单调接纳、拒绝态补行、细网失败保旧态，以及完整十二输入人工 IO、错 SHA/错态/错池拒绝和 summary 字节绑定；这不是新增研究的证明门。

本轮是否取得一个两网合格且曲率更低的真实状态，只能由随后的公开 Actions 报告回答。
