# 实际1372原矩阵的 G 坐标带状消费者：接口与误差账

## 1. 本次交付范围与身份

本条是 [节点G合同](2026-11-14-rawcell0-height-slope-node-gauge-contract.md) 的独立实现接口。actual42 在原1372矩阵上的全行 exact 缺陷仍大，根代理据实际回执选择下一种坐标表示。本条没有运行新矩阵形成、LU、整数残差或 nonlinear trial；终端失联，源码仅做逐行接口和代数核，**没有声称 AST、import 或运行已通过**。科学执行仍只在本公开仓库 Actions。

两份新文件没有修改任何冻结的原求解、捕获、整数核或矩阵绑定源：

| 文件（computations/） | UTF-8字节 | SHA256 | Git blob |
|---|---:|---|---|
| exact_20261114_rawcell0_gauge_system.py | 26256 | 24a51a4e804859bcdbed78b133599a073c6a0a890039e5fe5500281ef7e90b92 | 33b7bc06e0bebcb04fea6d1f29fd5dc489af03aa |
| exact_20261114_rawcell0_gauge_equilibrated_correction.py | 36045 | 16fca40ec0ff21a119ce1563241692248005ec6587af000efb968c5158ad9a00 | bd32c41686fd781ef669744cf6eb4e3e8780cbf6 |

入口必须运行于 GITHUB_ACTIONS=true、GITHUB_REPOSITORY=Rogerhu12/math-research-public。不会调用 Node、原 native、ODE、root、J、DN 或试步。

输入不是一个未来占位父场：直接读取实际28与41的原件，重建已在 actual42 中使用的原1372有限矩阵。实际42的坏方向不是本次初猜，不需要下载42的方向大包。

- actual28 result SHA：ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7。
- actual41 result SHA：6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf。
- 同一原1372矩阵 identity：e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521。
- M=112、K=224、原深度576、新深度1372，全部307552行保留；实际868个原RK步骤及原504个外段输入不改变。

冻结依赖为原步系统 adapter fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81、dyadic equilibration helper 8f5cb5da0826e3deedf935eca2e62b91c6628861804b2e66c6f853e9459e1dd3、depth-independent exact kernel 0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f，以及原28 binder b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390。仅为复用资源预算函数，另以30a467e8f08d73fcdcd8a69b2d911e0d9f57489c3397c21c775ed1ec4f6cabe6导入旧step driver；不会调用其main。

## 2. 唯一节点锚点与有限 G 定义

RawCell0GaugeSystem 的构造函数**包含实际矩阵形成**，只能在 Actions 执行，不能当成后继 trial 的只读身份加载器。

节点1至868逐一取其所属原step的field0；完整226输入状态SHA及profile/index/branch/x/h原bits交叉绑定。cut节点0只取stage0最后一步field3的root.g几何，并在Pi系数乘原出口port。节点869至1372为精确identity，不伪造r/w/μ。每节点只有一个anchor；不以相邻侧的略异r/w数值平均、替换或拼接。源μ保持各段window身份；实际 live 的orientation=1、spacing=2平铺键另作硬核。

对每个活动节点，先按明确括号在 NumPy longdouble 中形成

$$
r_2=r r,\quad r_3=r_2r,\quad r_4=r_3r,\quad
\alpha=r_4,\quad \beta_j=m_j^2r_3,\quad
\eta=\frac{((\varepsilon\sqrt{12})\mu)\rho_*}{r_4w}.
$$

随后将三个系数数组保存为明确的binary64 shadow；**这些保存字节定义本次实际坐标 G**。不是把格式化十进制或longdouble的padding当成真实数值身份。报告记录longdouble实际dtype、storage bytes、significand bits、指数范围、eps，以及最终cast变化/非零到零计数。若保存后的alpha或eta为零，变换本身不可逆，报告表示构造失败；不删模式或阈值化输入。

完整G保持原Q-all/Pi-all次序：

$$
G_{nj}=\begin{pmatrix}\alpha_n&0\\\beta_{nj}&\eta_n\end{pmatrix}.
$$

所有原r/w/μ/port原始bit记录、field packet压缩/解压hash、window身份及节点选择保存在 node-gauge-anchors.json.gz。系数为large-arrays/gauge-alpha.f64le、gauge-beta.f64le、gauge-eta.f64le。

## 3. 形成矩阵与边界

保存的原J与保存的G先提升到longdouble，用合同中的完整2×2分块公式形成所有224×224条目，最后每条目一次cast到binary64；不做逐模解耦、不抹非对角项、不宣称形成结果等于精确实数 $G_nJ_nG_{n+1}^{-1}$。

changed stages为0至868，共869块：第868块是旧stage72，左G、右I，必须支付完整混合接口。之后503块逐字复用原J。原504个外段输入全部保留，只是其中第一个的坐标表示改变。

新增 changed J 原字节为348823552B，存于 large-arrays/formed-gauge-changed-stage-J.f64le；其余原J不重复导出。每块源/形成SHA和原stage映射保存在gauge-matrix-binding.json.gz，所有均衡pass及LU都复用同一份保存字节，不能每次重新形成另一份J。

stage自身的 $-I$ 直接写入，不用一次舍入矩阵乘积 $-GG^{-1}$ 替代。cut从原式 $\delta Q_0+r_c=0$ 出发，显式左乘保存的alpha0，写成

$$
\xi_{u,0}+\alpha_0r_c=0.
$$

因此可以复用原带装配器的单位cut列。原cut residual、target和physical H全部保留；不把 $\alpha_0r_c$ 偷换为基于H重新计算的右端。远端G为I，原far graph、far residual及全部边界条目不变。

带宽仍为kl=112、ku=335，完整LAPACK band为1,377,832,960B。复用幂二行列均衡时，只对已形成的binary64候选矩阵逐次求entry exponent，最后一次ldexp形成带矩阵；所有损位另有原ScalingLedger。形成G/J的误差和随后dyadic scaling误差分别报告。

## 4. 原exact读回和真正用于求解的RHS

每次LU返回完整xi后，先恢复列幂二尺度，再用保存G的三角逆式在longdouble形成原坐标，最后保存binary64 delta。identity节点直接逐字复制，保signed zero。

$$
\delta Q=\xi_u/\alpha,\qquad
\delta\Pi=(\xi_k-\beta\delta Q)/\eta.
$$

先保存完整delta，再用原动态context和冻结整数核在**原1372 J/r、cut、far与原sigma**上遍历全部307552行，保存每行exact dyadic residual、每块最大值、全局有理最大值及原operand bits见证。选方向只比较这个原范数；转换后的norm、band因子成功或形成精度都不代替它。这里的exact仍只指保存浮点数组定义的精确线性模型，不是原 nonlinear flow 的精确导数。

冻结的exact evaluator同时会输出一份浮点RHS。为复用它而不复制全部整数点积，新wrapper给这份**从不送入LU的诊断RHS**统一行指数−2048。每原stage行至多224个有限binary64乘积，再加两个有限值，其量级严格小于 $2^{2056}$；这个辅助尺度避免诊断转换overflow，辅助underflow不能改变整数ledger。报告明确标记这份副产物。

真正用于LU的初始/校正RHS另从原base residual或完整exact ledger流式构造：

- cut：精确dyadic乘保存alpha0；
- 活动stage Q行：$\alpha e_Q$；
- 活动stage Pi行：$\beta_j e_{Q,j}+\eta e_{\Pi,j}$；
- identity stage及far：原exact行；
- 最后才乘实际求解行幂二尺度、取负、一次nearest/ties-even舍入为binary64。

因此没有先把e变成float再做G混合。原exact ledger、保存G、最终row exponents足以重建每个真正RHS。actual-gauge-rhs报告保全其完整数组hash、exact行作用流hash、round/underflow计数和样例。

有限迭代改进仍用同一LU。所有新delta都恢复原坐标后重新exact读回；若原norm不下降、更新相同、后继校正不可形成有限值，则保留此前完整读回的方向并记录原因。它不是native接受条件，也不承诺任何一轮会成功。

## 5. 输出与后继原试步合同

主result schema为 native-gauge-original1372-equilibrated-band-correction-v1。全量result写result.json.gz；短summary.json保初解/各轮原exact norm、最坏原stage映射、best iteration、方向/ledger/文件身份及错误。若小报告接近90KB，仅将详细收据移到已保全的全量result，不据文件尺寸中止科学步骤。

最终四个结果键保持清楚：

| result键 | 内容 |
|---|---|
| step_delta | 全部1373节点、原Q/Pi的binary64 delta |
| step_direction_checkpoint | 全部1373节点checkpoint |
| restricted_old_node_delta | 由oldToNew逐行选出的577节点原Q/Pi，逐bits可复核 |
| restricted_direction_checkpoint | 577节点限制checkpoint |

full checkpoint schema是 complete-original1372-direction-from-saved-node-gauge-v1；限制schema是 complete-original577-restriction-of-gauge1372-direction-v1。两者均保存新producer、original_input_binding、gauge_binding_file、gauge_matrix_identity_sha256、coordinate_identity_sha256、original1372_matrix_identity_sha256、M/K/depth/original_depth/step_depth/old_to_new，及rows={node,state,negative_zero_columns}和完整delta_float64le_sha256。没有把xi冒成原Q/Pi。

输出数组清单schema为native-gauge-original1372-output-arrays-v1。gauge binding schema为native-original1372-saved-height-slope-gauge-binding-v1，含alpha_beta_eta三份数组收据、anchors收据、complete_block_rows、formed_changed_blocks、original H/cut/far/sigma SHA及cut行乘子。

后继原nonlinear试步应只读旧RawCell0StepSystem及上述结果/收据，**不要实例化RawCell0GaugeSystem再次形成G/J**。它消费恢复后的完整原delta与577限制，原十试步/evaluate/H/far/σ保持；新旧线性norm仅作解释，不设新试步准入门。本入口不重算旧576长J缺陷；该量仍是另一个矩阵的诊断，不影响新方向是否需要原nonlinear读回。

## 6. Actions调用与资源

CAPTURE28及CAPTURE41必须分别指向通过已钉artifact下载器恢复的完整native-correction-capture和rawCell0-step-capture实际目录。不能只有公开小报告而缺原大数组。

```bash
python computations/exact_20261114_rawcell0_gauge_equilibrated_correction.py \
  --capture-directory "$CAPTURE28" \
  --step-directory "$CAPTURE41" \
  --step-result-sha256 6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf \
  --expected-original-matrix-sha256 e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521 \
  --equilibration-passes 3 --refinement-steps 3 --exact-workers 2 \
  --max-band-bytes 4294967296 --max-transformed-j-bytes 536870912 \
  --out "$RUNNER_TEMP/native-gauge-correction"
```

默认最多3次幂二均衡、3次改进、2个exact worker，CLI各自有明确有限上限。预算是资源上限，不允许丢行/节点/模式。预计主固定数组是一个约1.378GB带矩阵；是否LAPACK复制、实际LU bytes、RSS和runtime全部实报。逐块longdouble工作仅保存一块，新增changed J约349MB磁盘，不一次把全部变换J放进RAM。Python整数/BLAS workspace不冒作已精确计入的内存界。

所有large-arrays、G完整binding/anchors、full checkpoint和完整result应保在artifact；普通公开提交可保summary、factorization、每轮短exact摘要、manifest和源码身份。终端恢复前没有全大阵byte审计，本条不借实际41已审计声明新生成数组已审计。

此实现只产生下一有限表示候选。原g、H、far、完整频率、原ODE/RK步骤、native容差和全部科学完成标准均未放宽。
