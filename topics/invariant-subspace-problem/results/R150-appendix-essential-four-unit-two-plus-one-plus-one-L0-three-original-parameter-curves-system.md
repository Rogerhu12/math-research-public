# R150 / L0：三条原参数曲线的两几何变量必要理想

日期：2026-11-27（台北时间，UTC+8）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**状态：已完成原身份、完整投影和必要输入构造；尚无有理数单位证书。** 新输入只含 $(\lambda,w)$ 两个几何变量和一个饱和变量。只在实际返回 $I\,\mathrm{cert}=[1]$ 后，才可排除剩余 L0。

## 1. 三条曲线均来自同一个原点

[原八行矩阵](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-eight-by-eight-original-parameter-curve.md)给出 $C_{39,53}$，其常数坐标余子式的八列身份已乘回。另两条曲线是同一个原 P1 消元后

$$X_{34,52}=\operatorname{paidnorm}\operatorname{Res}_\rho(F_{E_1},F_{N_1}),\qquad
Y_{78,95}=\operatorname{paidnorm}\operatorname{Res}_\rho(F_{E_1},F_{E_{B,\mathrm{even}}}).$$

自含源重建原九式、同一个 $t=-\beta/\alpha$、八列余子式及这两条完整 QQ 结式。所有剥除因子均属于已付原单位，没有倒置任何未付参数首项。

| 曲线 | 参数次数 | 项数 | SHA-256 |
|---|---|---:|---|
| C | (39,53) | 1843 | `6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c` |
| X | (34,52) | 1580 | `519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68` |
| Y | (78,95) | 6379 | `c696ee10ac72763cbc2d9e01cd84cdda6bfd5116faa3262ddbf6f96490c54d33` |

三者只是必要条件；它们的交点可以包含不对应原 rho/t 的额外点。若该必要理想为空，则原点必不存在；若不空，仍须返回完整原 P/N，不能反向认作原解。

## 2. 只饱和已经支付的十个参数因子

从原物理单位中只取不含 rho 的六项：lambda、w、w−1、R=lambda−1−w、原 $C_{\rm mom}$ 及原 $P_0$ 分子；另加整边界已经排除的 W/G/K/V 四项。含 rho 的原单位和 alpha 不在这个参数饱和积内。

设这十项之积为 $S(\lambda,w)$，使用

$$I=(C,X,Y,zS-1)\subset\mathbf Q[z,w,\lambda].$$

每个剩余 L0 原点满足 C=X=Y=0 且 S 非零，故必能提升为这个理想的点。这里没有丢失任何未付的首项为零纤维，也没有使用多变量有限域单位性来推特征零。

## 3. 实际构造与唯一新 QQ 门

源：[2026-11-27-unit211-L0-three-original-parameter-curves-safe-slimgb-QQ-8542.py](../notes/2026-11-27-unit211-L0-three-original-parameter-curves-safe-slimgb-QQ-8542.py)，21,791 字节，SHA-256

`478dfef580829ad42e5e11cde0747df3af4742ca1f5bf613df4c34757de0362d`。

实际 `--build-only` 退出码 0，墙钟 68.485504 秒，源内 68.255040 秒，最大 RSS 133,448 KiB。构造时为 300 秒 alarm、8 GiB 地址空间、310 秒外部硬限。stdout 18,878 字节，SHA-256

`0fc8488ef12735efea827474bf9ead84ac2724e2941c8d86400b14526fc89b49`。

新完整 Singular 输入为 595,979 字节，SHA-256

`c0918f7705d703da4f4980f11dab7afa2b69acaa346c8291a710d314e33edaf1`。

[构造回执](../notes/2026-11-27-unit211-L0-three-original-parameter-curves-build-execution-8542.json)保三曲线、十单位及输入身份。专用 workflow `invariant-subspace-L0-three-parameter-curves-8542.yml` 先实际做独立 std 的 lift/product smoke，再只对这个新三变量输入做一次 1200 秒 QQ slimgb；最终须实际回乘原理想矩阵与证书。构造通过不算判空。

## 4. 已冻结的 C/X 直接投影

此前对新 C 与 X 的完整 w 投影确实运行过：源 SHA-256

`4bbb68e71eabaf23ae4591457da084d572d41715e331acd5584f603fd83785d7`。

它仅返回两曲线的原身份及投影 BEGIN，没有结式。240 秒源 alarm 未在本地原生计算内处理，外部 250 秒硬限终止，实际 250.007374 秒、RSS 118,808 KiB、exit −9。其 [精确失败源](../notes/2026-11-27-unit211-L0-C39-X34-direct-QQ-projection-failed-source-8542.py) 与 [小回执](../notes/2026-11-27-unit211-L0-C39-X34-direct-QQ-projection-failure-8542.json) 已冻结。

本次改用三条原必要曲线的完整两参数理想；不重跑旧 X/Y、C/X 大投影，也不从它们的有限域次数推 QQ 证书。


## 实际完整 QQ 门返回（2026-11-27）

run `45915015066` 的独立 std 检查通过；完整 slimgb 实际1200秒超时，仅有 BEGIN 标记，无返回基或单位乘回。driver墙钟 `1249.315264` 秒、峰值RSS `4456132` KiB、源exit1。原输入冻结，不提高时限重跑。完整源/输入/实际pull规则身份与小回执见[运行回执](../notes/2026-11-27-unit211-L0-three-parameter-curves-actual-QQ-timeout-8542.json)。
