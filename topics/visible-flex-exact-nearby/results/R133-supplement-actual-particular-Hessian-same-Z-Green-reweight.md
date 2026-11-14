# R133 续篇：特定 Hessian 与原同 Z Green 通道的实际重权

2026-11-14。**真实公开有向消费完成；负区 finite193 上界为 0.146218141878，仍未进入 $1/200$，不授 full PDE 响应。**

## 1. 实际过程

本仓库 [run 43618269135](https://github.com/Rogerhu12/math-research-public/actions/runs/43618269135) 完成 7 门，数学耗时 3.855568057 s，真实子过程 return code 0、10.000649509 s。只替换已证同方向 Hessian additive 并重权原正 Green 的右边界通道；没有再次传播主体源、解 Riccati 或计算任何旧 residual/projector cell。

证据目录为 notes/refined_Hessian_Green_ci/run-43618269135-1-particular-Hessian-cut-Green/。完整 native 是 native/complete-same-Z-particular-Hessian-cut-and-Green.json.gz，3,993,046 bytes，SHA256：
$$
\texttt{cd3dd5af3973053ad8d016f210123d493f25006dd8dcc11d5d64644a28c4add1}.
$$
小 summary 为 evidence/complete-particular-Hessian-cut-and-Green-summary.json，23,864 bytes，SHA256：
$$
\texttt{bfe332c6364660c25fe031ff6dc0b4267f48941c2158dba9942f4335f2de658c}.
$$
本文读取的仓库 process 快照 SHA256 是 37e6e68f60153284590f66667f99a935e32713283e4cad75457581da5e26a497。
artifact 名是 visible-exact-refined-Hessian-same-Z-Green-43618269135-1。

最后真实 pull 到 afadab246bd2ff5f20f938ab43ef1890f86b5c23；原实际 README 检查均没有差异。另读规则提交仍为 ee26c0a65a2e63c15f2ccfba6714181584416542。

## 2. 原输入与同一方向

原完整同 $Z$ Green、全 1977 格 cut 及同 $w_0$ Hessian 的 native 分别为：

| 输入 | SHA256 |
|---|---|
| 原同 $Z$ Green | eb34e2506c1cda9c1f53b4ef44605d02034e0cddf3feef44593edd635506bb18 |
| 全 1977 格 cut | 8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5 |
| 特定 $w_0$ Hessian | 9360555293def4b1803da05c5c432a8f737ed4f3d62ea2b84c89e7e236ff7650 |

实际下载的三个 artifact process SHA 按同一顺序是：

- 9b0708eacccb8fa5ee473fa26829f11eb5dd097fba9ad51931d1fcb17150fe8a；
- 55765c2954b872699fe60a8c81b62992841578233f12577f9b154a4db6873280；
- 0113de801ff7c0da2999bcfbf2e5e054560c2eb6dcd4278461305fc696213d5c。

它们和之后的仓库出版快照不是同一字节身份。消费者逐项核同一修补中心、连续 $Z$、准确 $w_0$、原 pilot、全部 source/worker/manifest 和原实际 child0。全部 6391 连续片、原接口及 $0-$ 腰端关闭保持不变。

## 3. 实际完整边界

原同向物理帽误差 $<2.418183102\times10^{-6}$ 及全部 14 项原费用准确保留。新特定 Hessian additive 为 $<1.033484771\times10^{-5}$，原 Hessian resolvent $<1.003854964897$。得到
$$
 E_{\rm mov}(w_0)<1.276235282\times10^{-5}.
$$
$Z_{\rm even}-w_0$ 继续乘原完整 moving **误差算子**的范数；独立 mean、全部 odd 行和 known high 均保留。

| 同一 $Z$ 输出 | 严格上界 |
|---|---:|
| 96 odd cut 行 | $4.120345670\times10^{-5}$ |
| 独立 mean | $1.276235303\times10^{-5}$ |
| 完整 97 行 | $4.313470180\times10^{-5}$ |
| 已知 full high 输出 | $4.136377748\times10^{-5}$ |

腰端原源 $<1.121483071\times10^{-15}$ 未改变。

## 4. 仅重权原右边界正通道

原通道采用的是一个明确的正**数值负荷常数**。新负荷上端除以该常数保存值的严格正下端，给安全比例
$$
 t<0.789998348514.
$$
它不是除以未知实际 boundary defect 的下界。原 right profile 的 $p,q$ 逐片乘该有向比例；其余三个通道原样保留并按完整 pair 和真实 $dr$ 积分。

| 通道 | 内段 $[0,9/10]$ 的 $L^2$ 上界 | 固定负区的 $L^2$ 上界 |
|---|---:|---:|
| 完整同 $Z$ 主体源 | $0.006513350907$ | $0.003051713268$ |
| 右边界源 | $0.305582916482$ | $0.143166428585$ |
| tiny trial jump 额外非负负荷 | $4.896727907\times10^{-11}$ | $2.294290956\times10^{-11}$ |
| 腰端源 | $6.019522904\times10^{-12}$ | $2.820848756\times10^{-12}$ |

逐片先叠加后的实际完整界是
$$
 \|e_{\le96}\|_{L^2(0,9/10)}<0.312096267009,\qquad
 \|e_{\le96}\|_{L^2(0,r_{\rm ph})}<0.146218141878,
 \quad r_{\rm ph}=2383968743003/10^{13}.
$$
角测度归一，独立 even mean 完整保留。该固定相位区间仍只属于当前背景，不能外推到改变的参数或最终非线性背景。

$1/200$ 门明确为 false。已知 high 主体源保持原完整表，known high cut 采用上表新界；未知 high 输入反馈及完整 high 响应尚须独立解决。此处所有数都是上界，不能解释成实际误差的下界。下一项沿同一已知方向继续 ordinary-only Hessian 和物理系数余项收紧。
