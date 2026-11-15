# 原 Koszul 外支撑的有限域 Smith 筛选接口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted，GPT-6 Astra Pro。
日期：2026-11-15。

## 1. 状态与唯一数学对象

本入口源码已冻结；本地执行环境不可用，因此没有声称已经 AST、编译或运行数学。第一次实际 Python 解析由本库 Actions 完成。入口无原生编译，使用已安装的 Python-flint 0.9.0 和标准库。

源码：`2026-11-15-r150-koszul-outside-field-smith-selector-789f.py`。

- Git blob：`44adf1efbea2ac5b1509e8132818c8cff00f4895`。
- 字节数：$23128$。
- SHA256：`6db545a1fb6ccb518d8c057f69dfa6d96ac37bafec67053483040f1ad31d7a1a`。

本入口只计算同一自然 $u$ 下

$$
O(u)=\operatorname{pr}_{J^c}\Phi(u)
 \in\mathbf F_{31}[[u]]^{1834\times1632},
$$

其中 $\Phi$ 是全部原 $136$ 个标准 Koszul 对乘
$1,m_0,\ldots,m_{10}$ 的 $1632$ 列。列顺序严格为
$i<j$ 字典序，其内乘子顺序为 $1,m_0,\ldots,m_{10}$；
第 $i$ 个方程来源上的项是 $+F_j$，第 $j$ 个来源上的项是 $-F_i$。

[扭子模注入及所选子式证明](../results/R150-appendix-koszul-outside-torsion-embedding-and-selected-minor-test.md)
给出本次有限域截止：$O$ 的 $29$ 个正指数全部至多 $21$，总长度至多
$243$。这只使用已经完成的同一个所选 $B$ 的有限域指数，不把这些界转成
特征零的最大指数。

## 2. 临时输入及绑定

使用当前 run43702348535 的已成临时文件，无需恢复 Release、无新增工件下载。
实际命令为：

~~~sh
python {scripts}/2026-11-15-r150-koszul-outside-field-smith-selector-789f.py \
  --pairing-root {work}/same-source-koszul29-second-pairing \
  --primitive-equations {primitive} \
  --rebuild-root {work}/selected-natural-u-rebuilt \
  --paid-schur-summary {scripts}/43702348535-selected-natural-u-minimal-rebuild32.json \
  --out {work}/koszul-outside-field-smith \
  --seconds 120 --memory-mib 1024 --maximum-degree 21
~~~

最后一个已付小回执应作为本步文本 source 放入 scripts；不要把 stepId
误作重建目录。真正重建目录是 `selected-natural-u-rebuilt`。

| 输入 | 字节数 | SHA256 |
| --- | ---: | --- |
| 原 primitive equations gzip | 65159 | 44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe |
| rebuilt-first/same-original-natural-constant-and-first-coefficients.json.gz | 20580 | 7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1 |
| rebuilt-inputs/same-selected-original-source-indices.json | 21285 | 20373c07422701e37b9226fe1fe72cb8ee1e7848df505ebbacd92cf818093c2a |
| 主线已付 minimal-rebuild32 小回执 | 26242 | e57d4bc56bbd50e1d1700b819a3f5f6499c92b885788ec3fe55089b5a6755657 |

原 equations 解压后 SHA256 同时核为
`fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3`。

pairing-root 内复用以下五个现成文件：

- reconstructed-source-model/exact-original-koszul-outside-model.json.gz；
- reconstructed-source-model/exact-koszul-sparse-core-and-dag.json.gz；
- reconstructed-source29/koszul-exact-rational-support-receipt.json；
- reconstructed-source29/exact-unit-block-profile.json；
- 上述回执记录的完整 model/core/profile 身份。

该链要求实际 source binding 严格等于

~~~text
2d9b068281400ec635fc2c912edf29e59d2bec1e3686bf6c3f6abd6ac01890f2
~~~

程序从 model/core 的实际字节、旧 support source SHA、旧 helper SHA、原 point SHA
重建这一 binding，并逐字比较已付回执的 inputIdentity。profile 的实际
SHA/bytes 必须与该已完成回执记录一致。这里不拿旧 run43679903558
同名文件的 gzip SHA 代替当前会话的实际文件。

自然第一系数 binding 必须是
`c11dd73f0b8f469a8c1abee84de0b8ff7a38906a992376a16129a44fcad8607b`；
已付所选 $B$ Schur binding 必须是
`43124d7d621b24353e3686cb1db8932ee6259822f22c1dbb1f8e0cd1d7b54600`。

新语义 binding 包含当前源码和全部实际输入身份，排除绝对目录、预算及请求最大
次数。因此同源码、同输入、同 out 可直接接续。

## 3. 完整原来源检查与系列递推

程序从原整数 equations 重建全部自然系数 $F_0,\ldots,F_{10}$：

$$
F_{N,\mathrm{linear},k}=[s^{10-k}]F_N,\qquad
F_{N,\mathrm{quadratic},k}=
 \begin{cases}F_{N,\mathrm{quadratic}},&k=0,\\0,&k>0,\end{cases}
$$

而 Gamma 的二次项用 $[s^{5-k}]F_\Gamma$，全部线性项严格为零。
它逐项核对既成原 $F_0/F_1$，并重建所有 $6188$ 个来源坐标的
$\Phi_0$，与当前已付原模型完全相等后才计算外支撑。

现成 core 的剥离 DAG 必须为空，变量必须恰为 $0,\ldots,1631$。
每个 core 行必须等于其对应的原整数外支撑行，不能把曾经除去 $31$
因子的有理行操作解释成有限域操作。程序重放现成 $1603$ 原单位
行列 profile，真正求 $U^{-1}$ 并完整核对 $UU^{-1}=I$。
它不重作旧 $1603$ 有理求解，也不重做原 $4318$ 维正常形。

令 $C$ 为这 $1603$ 个单位来源列、$F$ 为余 $29$ 列、$P$ 为所选单位行。
完整规范来源图满足

$$
X_0|_F=I,\qquad X_0|_C=-U^{-1}P O_0|_F,
$$

以及对 $k\ge1$，

$$
X_k|_F=0,\qquad
X_k|_C=-U^{-1}P\sum_{i=1}^{\min(10,k)}O_iX_{k-i}.
$$

每层重新保留全部原 $1834$ 行的

$$
R_k=\sum_{i=0}^{\min(10,k)}O_iX_{k-i}.
$$

全部 $1603$ 个单位行必须为零，余 $231$ 行就是完整矩形 Schur 系列。
常数层必须全部 $1834$ 行为零；原 $36$ 个自由来源坐标上的
$\Phi_0 X_0$ 必须秩 $29$。该检查连同 $O_0$ 的单位块还实际证明
$\Phi_0$ 满列秩 $1632$，没有把 $29$ 个系数向量只当像的维数。

最后对完整 $231\times29$ 系列逐次做常数单位 Schur、除 $u$：
每层保留全部未消行，不丢自由余核的 $202$ 行；每个小单位系列逆都逐次乘回。
请求次数 $21$ 包含 $u^{21}$，即 $22$ 个系数。
若到这里仍有未定正指数，入口判失败，不能预填已知截止替代实际结果。

## 4. 真实检查点、预算和长期输出

数学预算 $120$ 秒、地址空间 $1024$ MiB；无原生编译。
接口允许在同一语义 binding 下以较小次数先保存或以新预算续接，
源码本身的上限为 $300$ 秒、$2048$ MiB、次数不超过 $21$。

单位逆先完整保存并绑定。之后每个次数保存三个完整临时数组：

- outside-source-k.bin：$1632\times29$；
- outside-residual-k.bin：$1834\times29$；
- outside-schur-k.bin：$231\times29$。

每个数组含版本 magic、域、次数、完整维数、语义 binding 和全部 canonical
field entries。三文件保存成功后才原子更新 outside-complete-jet-ledger.json。
恢复只接受逐项 SHA/bytes 匹配的完整层；中断的下一层不会冒充完成。
SIGTERM/SIGINT 在安全检查点请求退出；完成的层继续可用。

大数组只留当前 job 临时目录。永久保存的只有源码、参数、运行身份和小回执：

`koszul-outside-field-smith-receipt.json`。

完整结果要求：

- status 为 completed，outcome 为 complete-outside-field-smith；
- allOriginalNaturalCoefficientsMatched；
- all6188ConstantKoszulCoefficientsMatched；
- actualOriginal1603UnitVerified；
- originalKoszulConstantRank1632Verified；
- all29OriginalConstantSourcesIndependent；
- all1603OriginalUnitJetRowsZero；
- all1834OriginalOutsideJetCoordinatesRetained；
- all29FreeFamilyCoordinatesVerified；
- completeOutsideSmithLengthComputed。

参数中保存完整小 Smith steps、全部 $29$ 个正指数、当前临时文件身份和输入绑定。
超时或未满请求次数只返回 checkpointed-outside-field-jets，不给完整长度结论。

characteristicZeroSmithComputed 和 leadingCoefficientUnitProved 始终为 false。
本次任何有限域筛选值都不能直接宣布特征零最高系数为单位；后继必须使用上述
扭子模证明中的实际特征零长度与全原矩阵下界夹逼。
