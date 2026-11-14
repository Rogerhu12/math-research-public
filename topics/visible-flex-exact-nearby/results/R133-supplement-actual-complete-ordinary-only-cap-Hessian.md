# R133 续篇：完整同向 ordinary-only Hessian 的实际结果

2026-11-14。**公开计算真实完成；同一 $w_0$ 的 Hessian additive 降到 $1.348921723\times10^{-6}$。这仍只是一项已知源上界，不是完整 PDE 逆或最终响应误差。**

## 1. 实际运行和完整证据

本仓库 [run 43618931236](https://github.com/Rogerhu12/math-research-public/actions/runs/43618931236) 通过全部 11 门。实际数学耗时 114.579596371 s，子过程 return code 0、120.003394661 s。

目录为 notes/ordinary_only_cap_Hessian_ci/run-43618931236-1-same-w0-ordinary-only-cap-Hessian/。完整 native 为 native/complete-same-w0-ordinary-only-cap-Hessian.json.gz，1,010,976 bytes，SHA256：

b1ffc21737ba45d1ef8823af9dccc0baba8b100a1169b60c69f6a7a5d1cfda6c。

小 summary 为 evidence/complete-same-w0-ordinary-only-cap-Hessian-summary.json，11,388 bytes，SHA256：

f6640ebc877a6a68832944deda15103013609dd1fceb9927859426a3bf46349a。

本文读取的仓库 process 快照 SHA256 是 989e72f6ce887a7f9b60f645803e437383dab87c2245b7d34d7e82e5084cc0c7。最后真实 pull 到 e1f98ab7effd9094a5373ebdbcf7c22299e2f109，根及课题 README 的实际检查均无差异；另读规则提交保持 ee26c0a65a2e63c15f2ccfba6714181584416542。artifact 名为 visible-exact-ordinary-only-cap-Hessian-43618931236-1。

## 2. 同一试解、完整 mean 和新的源表示

原方向、原全帽 Hermite 数组及两侧导数逐字节保持；仍是全部 97 个正交 even 输入槽和 257 个物理输出槽。原真实入口 $9/10$ 的极短首格外推保留。

全部 1341 个原局部胞元和 1977 个真实 Hermite 交集完成新的角导 Legendre 范数。此前成功 native
9360555293def4b1803da05c5c432a8f737ed4f3d62ea2b84c89e7e236ff7650
保存的 $t_B,t_C$ 全格范数逐行复用，没有重复这些旧计算。实际原 artifact process 的 SHA 是
0113de801ff7c0da2999bcfbf2e5e054560c2eb6dcd4278461305fc696213d5c。

本次直接用精确恒等式
$$
 D^2\Psi[R,t]=-e\,t_\theta+{\cal Z}t.
$$
因此收费 $E_\infty\|t_\theta\|+Z\|t\|$，不先改写为 divergence，也不再收那一表示产生的 $E_1t$。乘法保留全部高输出。mean 的角导准确为零；mean 的原 $Z$ 反应和独立输入 mean 全部保留。

## 3. 实际有向预算

两个完整 ordinary 源范数为
$$
 O_B<4.099766064\times10^{-8},\qquad
 O_C<3.706278030\times10^{-8}.
$$
仅用原已付 ordinary B/C Green 增益，得到
$$
 E_H^{\rm ord}<1.343741646\times10^{-6}.
$$
原完整 Hessian resolvent 仍为 $<1.003854964897$，于是
$$
 A_{w_0}^{\rm ord}<1.348921723\times10^{-6},\qquad
 \varepsilon_{\rm mov}(w_0)
 \le \frac{\varepsilon_{\rm phys}(w_0)}{1-\chi_H}
     +A_{w_0}^{\rm ord}.
$$
新的完整 additive 与此前完整四通道 additive
$<1.033484771\times10^{-5}$ 之间取 min。没有将不同分解的个别源项混接，也没有改变未知输入的 Hessian feedback 或 moving 误差算子。

## 4. 后续消费范围

这份结果可替换同一 $w_0$ 的 additive，然后沿原完整 true cut odd/mean/high 转换和既成正 Green 右端通道消费。$Z_{\rm even}-w_0$ 仍须乘原完整 moving **误差算子**的 norm；其余主体源、腰端、projector jumps 和高输入反馈仍完整保留。

它没有重算 target、primitive、原物理帽 residual 或外端计算，也没有单独授予 true cut source 或 finite193 误差。新的物理帽系数域细化与全无限系统仍分别推进，不能用本篇预算下降代替主目标完成。
