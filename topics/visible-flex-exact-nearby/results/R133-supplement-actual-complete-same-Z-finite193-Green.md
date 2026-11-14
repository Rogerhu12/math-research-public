# R133 续篇：同一连续 Z 的完整 finite193 已知源 Green 实际验收

2026-11-14。**真实公开计算完成，所得上界尚未进入 $1/200$。完整无限 PDE 响应、high 反馈及参数 Schur 仍未由本篇证明。**

## 1. 实际数学执行与身份

[公开运行 43616648792](https://github.com/Rogerhu12/math-research-public/actions/runs/43616648792) 执行了真实数学子过程，并非仅 eligibility 检查。9 门全部通过；数学耗时 13.443182669 s，真实子过程 return code 0、15.000678911 s。

证据目录是
`notes/same_Z_Green_ci/run-43616648792-1-same-Z-Green-body-43613560173-cut-43615251195/`。
其 `evidence/complete-same-Z-Green-summary.json` 为 6,104 bytes，SHA256
`6874be5a5bfe30d5c67f037d15f9e97989ee170d98d927ed577f368b6cd264f2`。

完整逻辑 native
`native/complete-finite193-same-Z-known-source-Green.json.gz`
为 7,154,812 bytes，SHA256
`eb34e2506c1cda9c1f53b4ef44605d02034e0cddf3feef44593edd635506bb18`；
它按 4 个原字节片及 lossless manifest 保存，没有截去 6391 段 profile。
本文读取的仓库 process 快照 SHA256 为
`524231ae273326d1707111af12f51a40a00501bded1b79208a61bac5ba2de156`。
artifact 名是
`visible-exact-complete-same-Z-known-source-Green-43616648792-1`。

最后真实 pull 到 `4183d7d91631010e2ead9495f74a8cf7579b142d`，
四次根/课题 README 检查均无差异，另读规则提交为
`ee26c0a65a2e63c15f2ccfba6714181584416542`。

## 2. 所消费的完整源与边界

输入保持三个完整原证书：

| 输入 | native SHA256 |
|---|---|
| 原完整 finite193 Green | `fd6c1f4baa4ec86aab08d4925a0ec9565c3791cbe470b77c2e41549d8f071de6` |
| 全 7721 行连续 $Z$ 主体源 | `365f0763d8f4c87182507c4372a3be055624607a77d818a084471b368b33d32e` |
| 全 1977 格同一 $Z$ 真实边界 | `8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5` |

实际 artifact process SHA 分别为
`297cb4c9b8f58bbaacbcf1d0be594f43ea385420f8ea58fbb14e83bf84a63a1c`、
`56c84147351d56b262a17ae0cbf96e18c6525083d72bd51e2f590620dc6e5168`、
`55765c2954b872699fe60a8c81b62992841578233f12577f9b154a4db6873280`。
这些是实际下载的 artifact 快照，不冒用之后仓库 process 的出版快照。

原 Riccati ports、5970 个 projector、全部真实接口、0− 腰端虚接口和两端 lifting 准确复用。只有新的完整已知源通道被传播；没有重算这些逆门或原 body/cap 残差。所有源与两边界均属于定义
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`
的同一个连续 $Z$。

## 3. 实际误差分解

完整内 BVP 是 $[0,9/10]$。相位所需普通 pair $L^2$ 只累计到固定安全上端
$$
 r_{\rm ph}=\frac{2383968743003}{10^{13}}.
$$
独立 even mean 包含在 pair 中。原加权态按每个真实连续片的完整权恢复到普通 pair，再按真实 $dr$ 积分。

| 通道 | $[0,9/10]$ 的 $L^2$ 上界 | $[0,r_{\rm ph}]$ 的 $L^2$ 上界 |
|---|---:|---:|
| 完整同一 $Z$ 主体源 | $0.006513350907$ | $0.003051713268$ |
| 原 tiny trial jump 的额外非负负荷 | $4.896727907\times10^{-11}$ | $2.294290956\times10^{-11}$ |
| 同一 $Z$ 腰端源 | $6.019522904\times10^{-12}$ | $2.820848756\times10^{-12}$ |
| 同一 $Z$ 完整真实右端源 | $0.386814626963$ | $0.181223706169$ |

原 trial jump 仅作为安全的额外非负负荷，没有将其说成连续 $Z$ 的实际跳。表中的每个通道均有完整 6391 段原位 profile。

逐格先叠加四通道、再积分所得总界为
$$
 \|e_{\le96}\|_{L^2(0,9/10)}<0.393327977489,\qquad
 \|e_{\le96}\|_{L^2(0,r_{\rm ph})}<0.184275419462.
$$
两区普通 pair 的共同 sup 上界为 $3.197292070$。
这里 $e_{\le96}$ 是本篇明定的有限压缩响应误差，不冒称无限系统的真实误差。

## 4. 当前未闭合的门

完整 finite193 源消费已经成立，但上述负区上界不小于 $1/200$，native 中相应 gate 明确为 false。主体源通道已小于 $1/200$，右端通道仍主导；这为下一次定向收紧指出实际位置，不是主目标完成声明。

已知 high 主体源与 cut high 输出仍分别保留。全区 high 主体 $L^2<1.961162401\times10^{-6}$，内段 $<1.155272970\times10^{-6}$，固定负区 $<2.308004471\times10^{-7}$；已知 cut high 输出 $<5.231670385\times10^{-5}$。这些是源上界，不能代替未知 high 输入反馈或 full high 响应。

固定负区上端和当前背景也未转授到改变的 $\nu$、$\delta$ 或真正非线性背景。后续可以仅替换经过严格验证的同向边界费用、重权原正 Green 边界 profile，保留其余通道及全部接口；若要使用有符号/有方向边界响应，必须另外完整认证其传播。
