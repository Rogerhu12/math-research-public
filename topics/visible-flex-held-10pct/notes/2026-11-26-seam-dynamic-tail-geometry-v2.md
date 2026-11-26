# 按实际 native 模数定义的全尾几何入口 v2

维护：Astra-held10-06bbeb39-20261126 / seam_geometry。2026-11-26 UTC。

## 范围与当前状态

这组独立 v2 入口解除新实际候选在模式数上的工程阻塞。原 M24/512/degree192 入口、原场数组及证书均不改动。当前没有新的完整 $\lambda=1$ actual-DN 场，也没有执行新场的全尾几何认证。本文件给出的模式数示例只是整数公式的结果，不是新场实验数据。

新增源是：

- `seam_tail_spectrum_v2.py`：实际有限维度和完整频率列表的固定合同；
- `seam_export_shared_r_tail_v2.mjs`：同一原累计 mean 下的完整共享 $R$ 节点；
- `seam_export_tail_geometry_v2.py`：accepted packet、真实 native 输入输出、物理 port 与上述图的绑定；
- `seam_certify_tail_geometry_v2.py`：每一实际 stage 和本次深端 collar 的连续度量、曲率与条件几何界；
- `seam_run_tail_geometry_v2.py`：先 stage 0、再其余全部 stage 的同合同父入口。

v2 复用的是已读过的精确 Hermite、Fourier 合并、Bernstein 和真实背景公式；所有扰动系数与数值界都取自本次实际输入。原函数库的 M24 命令行入口不被调用，也不把其旧数值执行记录推广给新模式数。

执行环境恢复后，五份源码从审阅提交 `7f6978a50aab17063286852925c7706dd7ee32e7` 的缓存字节恢复，逐项 Git blob 核对相同。Python 3.12.14 编译、Node v24.22.3 模块语法检查及三个命令行入口的 `--help` 均真实 exit 0。小整数频率核对保留各实际最高状态模式，两个不完整带宽例被拒；详见 `2026-11-26-seam-dynamic-tail-source-checks.json`。这些是源码与维度接口检查，没有输入实际尾包，没有新场几何认证。

## 1. 随实际输入冻结频率列表

从真实 accepted packet、完整 checkpoint、原 native metadata 及 ABI 交叉核验

$$
M,\qquad N,\qquad s=3,\qquad n_q=N/\gcd(N,s).
$$

此版本仍限本课题原三重对称、原物理 depth $8$ 和相同 R58 背景；它不更换目标度量或原求解门。shooting 的实际全部 stage 数来自本次完整 checkpoint，不按旧文件名推断。

令实际选定的平面带宽为 $D$，要求

$$
3M+1\le D\le \left\lfloor\frac{N-4}{2}\right\rfloor.
$$

默认选右端；也可在这次实际输入上明确提供 `--degree`。选择方式、实际 $D$ 和全部有符号频率列表写进 `spectrum-contract.json`，随后由所有 stage、manifest、证书和 resume 合同同时绑定，不能在 stage 0 与后续 stage 之间更换。最终 $D$ 只在真实输入上确定。

完整列表为

$$
\mathcal P_D=\{m\in\mathbb Z:|m|\le D,\ m\equiv1\pmod3\},
\qquad
\mathcal H_M=\{0,3,\ldots,3M\}.
$$

$D\ge3M+1$ 保证每个物理状态模式映成 Cartesian 平面时的 $1\pm3j$ 全部保留。$N\ge2D+4$ 保留原导出器的角网格余量；它本身不是对连续源 Fourier 尾的误差证明。

例如，实际输入若为 $M=32,N=512$，默认 $D=254$，$\mathcal P_D$ 有 $170$ 项，$\mathcal H_M$ 有 $33$ 项，每个节点两jet的每阶共有 $203$ 个实系数。这里既没有沿用 degree192，也没有强行令 $D=8M=256$ 而违反网格条件。若 $N$ 改变，实际合同和有限表示必须一起重新登记。

## 2. 一个明确的新有限 Cartesian 图

原 native 的 $2M$ 状态、原 worker 的完整请求 $H$、真实 factor 与原 Python/NumPy 计算顺序保持逐项绑定。原非旋转零模仍是同一次 native evaluation 的完整累计 mean chain；既不把它改成旋转背景，也不新增独立 mean 参数。

在每个实际节点，平面系数由原 $N$ 个角样本按声明的有限列表计算；高度保留全部 $\mathcal H_M$。这些计算出来的 binary64 系数及半径节点被声明为精确二进制有理数。相邻节点间的图是这些完整 0、1、2 jet 的精确五次 Hermite 多项式。使用数值 $rr$ 的地方只把它作为这张有限图的节点参数，绝不称为原未投影 PDE 的精确 $rr$。

该定义通常不等于未投影连续 source evaluator。v2 不把 DFT 截断、离散积分或导数近似误差设为零。可验证的命题是：**对这张明确声明的新有限图，重新直接计算相对于同一个 R58 真背景的全部度量与曲率误差。** 所需精确等距、连续族与极限相容论证不会由这个有限证书自动获得。

所有有限 stage 的端点采用本次实际选定的唯一节点表，包括原 cut、每个内部边界和最深端点。节点半径与全部 Cartesian 两jet逐字复制；跨 stage 不把“很接近”当作共同节点。stage 0 完成后，后续导出直接读其原 `boundInput`、完整频率合同及原节点，保留 stage 0 数据与证书的字节，不需重写别名数据。

深端 collar 按本次最深节点的完整 $\mathcal P_D\cup\mathcal H_M$ 构造。同一精确 Hermite 基逐系数验证外端两jet一致、内端两jet为零；无固定 `0..72` 高度列表，没有丢弃提高 $M$ 后的最高模式。内侧继续到相同 R58 旋转 cuff/disk。

## 3. 原连续多项式证明为何不依赖 M24

对任一径向段，所有实际模式均进入精确多项式数组。角导数由对应的真实整数 $m$ 乘出；Bernstein 范数使用完整频率加权和。线性 Gram 项按实际相同频率合并；低频二次项可精确合并，余下高频二次项由所有被保留高模式的范数和显式控制，没有隐含 degree192 的截断。

如果 $\mathcal P_D$ 的最大绝对频率为 $P_{\max}$，完整 Gram 展开的频率不会超过

$$
2\max(P_{\max},3M).
$$

这是有限乘积的范围说明；实现使用频率字典与严格余项和，不按这个上界删去项。背景的真 $w,w_R$、单调 $R$ 覆盖、全段严格度量门与曲率预算保持原合同。新的每一段必须重新通过，新的深端 collar 也必须重新通过。

同一原 mean 也进入绝对高度放置。仍用

$$
z_b=Z_c+\mu_{\mathrm{cut}},
$$

其中 $Z_c$ 必须由实际新前缀的真实 mean1168 原函数提供。本入口只保留原条件窗口，不能从一个 accepted 包或单独的高度常数相接推出公共 Cartesian $C^2$ 接缝、full-H 解或整体闭曲面。

## 4. 改变 N 或 degree 时的精化账目

提高 $N$、$M$ 或改变 $D$ 通常得到另一张有限图。相同连续 R58 背景不表示两张扰动图相同，原 native 累计 mean 也不能被替换为相同常数。

若要比较两次表示，须取两图全部精确 $R$ 节点及深 collar 端点的并集，在每个公共径向段上把两组 Hermite 多项式精确重参数化。对平面和高度频率分别取并集，缺少的模式系数为零。然后对实际多项式差的每个径向、角向导数求 Bernstein 范数和：

$$
B_{ab}(J)=
\sum_{m\in\mathcal P\cup\widetilde{\mathcal P}}
 |m|^b\|\partial_R^a(p_m-\widetilde p_m)\|_J
+
\sum_{m\in\mathcal H\cup\widetilde{\mathcal H}}
 |m|^b\|\partial_R^a(h_m-\widetilde h_m)\|_J,
\qquad a+b\le2.
$$

两图使用相同真实背景时，背景项可以符号消去；它们的实际非旋转 mean 差必须保留。若输出只相对于各自 $Z_c$ 定义，则常数位置差还含真实 $\Delta Z_c$。绝对 $C^2$ 精化需要由新前缀另付这一项，不能将两次高度原函数自动视为同一个数。

本 v2 入口直接认证每张有限图，不自动输出上述跨表示差界，也不自动声明 $C^2$ 极限。这一待付项目被明确保留，不能拿“同 $g$”或离散采样收敛替代。

## 5. 实际调用

先取得同一真实 accepted packet 对应的原 native records、物理 port 和完整高度引用，之后调用：

~~~bash
python "$TOPIC/scripts/resume_20261126/seam_run_tail_geometry_v2.py" \
  --tail-response "$PACKET" --source-port "$PORT" \
  --source-topic "$ORIGINAL_TAIL_SOURCE" \
  --native-record-dir "$NATIVE_RUNS" \
  --height-reference "$HEIGHT_TARGET" \
  --height-reference-key candidate_H \
  --warm-factor 1 --height-arithmetic numpy \
  --phase stage0 --outdir "$WORK/new-tail-geometry-v2"
~~~

只有这些文件实际存在且通过其原接受门时，这条命令才是有效执行。warm 输入须给它真实的 factor、引用字段和算术，不能倒推完整 $H$。随后保持原参数与同一输出目录，把 `--phase stage0` 改成 `--phase all --resume`；程序保留 stage 0 并处理所有其余实际 stage。

完整数组、逐段证明、native 文件及大 summary 留在 runner；仓库只收源、此范围说明和未来实际执行后的小证据。该版本的编译与实际输入执行状态须以单独小记录为准，不能将本入口说明当成成功证书。


## 6. 同一完整谱的切口修补读取器

独立 `seam_certify_cut_attachment_v2.py` 使用上述 v2 完整输入门，再逐项绑定实际 stage0 的 schema、全部频率与同一 spectrum contract，以及对应的新连续证书。其余真实预算提取、原 Hermite 两jet修补和度量/曲率合并公式均与已审原件相同；未知图定义不会进入修补。源码 SHA-256 为 `2845cc1ef39d41bff6443a08078cd84bb9875de1ca084549cfec5b972c4f0bd3`；本地真实编译和 `--help` 均 exit 0，尚未输入实际新尾场。

## 实际 factory 与 checkpoint 参数含义修正

原 native factory 保留输入 `depth=8` 与 `linearMethod=matrix`；shooting checkpoint 则把 `depth` 覆盖成实际子段数，另存 `physicalDepth=8`，并把方法标成 `stable-momentum-cusp-subdivision`。不能逐键直接比较这两个完整字典。导出器现按原 stage-core 的 13 项覆盖表达式分别核对原输入与导出字段，其余物理参数保持逐项相等；原 port 的 22 项也逐项绑定。

运行中的 stage-core 已经原 chord/native 安装器修改，因此历史全文件 SHA 仅作语义来源，不作运行文件的相等门。实际 packet、native manifest 和磁盘文件三方必须同 SHA；在该实际文件内核对全部四个参数构造区和二个原 return（有 chord 时另一个 return）的完整表达式。未被安装器改的另外三个 factory/subdivision 源仍保原 SHA。该修正没有改变方程、参数或任何残差验收阈值。

[实际源码级检查](2026-11-26-native-factory-checkpoint-parameter-checks.json)记录原 chord 安装结果再加原 native 的三项 literal patch 后仍通过上述表达式核验，Python/Node 检查通过。没有使用已接受的新 tail packet，没有新场几何数值界。当前导出器 SHA `5b318a169ef74b29d10295bdc0da764e86b437cd447ca83045248c5fb576408a`。
