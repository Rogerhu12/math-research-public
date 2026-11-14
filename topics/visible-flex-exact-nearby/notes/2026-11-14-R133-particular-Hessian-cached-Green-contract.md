# R133：仅替换同方向 Hessian 费用并重权已成正 Green profile

2026-11-14。新消费者只读三份真实完成 native：同一连续 $Z$ 的 6391 段 Green（run 43616648792）、完整 1977 格方向与两边界（run 43615251195）、同一 $w_0$ 的完整特定 Hessian（run 43616252389）。所有新有向算术仅在本公开仓库 Actions 执行。

## 1. 同一物理误差与完整边界

令 $E_{\rm phys}$ 为完整 1977 格原 14 项物理费用之和，$H$ 为既成 Hessian resolvent，$A_{w_0}$ 为新的特定方向 additive。沿同一固定输入有
$$
 E_{\rm mov}(w_0)\le H E_{\rm phys}+A_{w_0}. \tag{G.1}
$$
两边界 native 中的旧合法 $E_{\rm mov}(w_0)$ 也保留，可对两个独立合法标量上界取 min。不得以新的特定方向 additive 代替未知输入误差算子的 norm。对完整连续方向 $Z$：
$$
 E_{\rm mov}(Z_{\rm even})\le E_{\rm mov}(w_0)
       +\|\mathcal E_{\rm mov}\|\,\|Z_{\rm even}-w_0\|. \tag{G.2}
$$
这里 $\mathcal E_{\rm mov}$ 是原完整 moving 误差算子，不是完整帽算子；它的原范数准确不变。

设原 cut 消费者保存的三个前置误差为 $a_{\rm low},a_{\rm mean},a_{\rm high}$，物理到 moving 行增益为 $S$，even 输入范数为 $W$，同一 $Z$ 的 nominal odd 和 mean 为 $n_o,n_m$。完整边界界仍为
$$
 b_o=n_o+a_{\rm low}W+S E_{\rm mov},\qquad
 b_m=n_m+a_{\rm mean}W+E_{\rm mov}, \tag{G.3}
$$
$$
 b_R=(b_o^2+b_m^2)^{1/2},\qquad
 b_{\rm high}=a_{\rm high}W+S E_{\rm mov}. \tag{G.4}
$$
独立 mean、完整 96 odd 行和已知 full high 输出均保留。左腰 $b_0$ 完全复用。原入口的 $9/10$ Hermite 外推已由此前真实 native 支付，本消费者不重新求值。

## 2. 原正 Green 通道的合法重权

完整原同 $Z$ Green 已逐片保存四个独立正通道：主体源、原 tiny jump 的额外非负负荷、腰源、真实右边界源。每个通道的加权 $p,q$ 上界对应同一个已认证连续 operator、全部 projector 接口和腰端 $0-$ 关闭。

设原右边界通道使用的**已选数值负荷常数**为 $B_{\rm old}>0$，其保存值的有向下端是 $\underline B_{\rm old}>0$。若新的严格负荷上界为 $\overline B_{\rm new}$，取
$$
 t=\operatorname{up}\!\left(
       \frac{\overline B_{\rm new}}{\underline B_{\rm old}}\right). \tag{G.5}
$$
原右端单位响应是同一正线性 Green 的响应，故原每片已证 $p_R,q_R$ 可分别改成
$$
 \operatorname{up}(t p_R),\qquad \operatorname{up}(t q_R). \tag{G.6}
$$
这里除的是已记录的正数值常数，绝不是未知实际边界 defect 的下界。即使实际 defect 为零，该重权仍成立。以保存的负荷下端为分母只放宽界，不损失旧 profile 的舍入费用。

其余三个通道原样保留。此步不重解 Riccati、不重新传播主体源，也不重新计算任一 projector 或 physical cap 残差。

## 3. 完整普通 pair 范数

对原第 $i$ 个真实连续片，正权 $\rho_i(r)$ 的两端为 $\rho_{i,-},\rho_{i,+}$。保存 profile 已覆盖片内全部 $r$。四通道相加得到 $p_i,q_i$ 后，
$$
 \|h(r)\|_{\rm pair}^2
 \le \max(1,\min(\rho_{i,-},\rho_{i,+})^{-1})^2
       (p_i^2+q_i^2). \tag{G.7}
$$
按原真实片长积分，恰核全部 6391 片无缝覆盖 $[0,9/10]$。相位普通 $L^2$ 只累计到已被原 profile 准确切开的
$$
 r_{\rm ph}=2383968743003/10^{13}. \tag{G.8}
$$
完整 even mean 与所有角槽均在 pair 中。这个当前背景上端不转授到改变的 $\nu,\delta$ 或非线性背景。

## 4. 实际身份、恢复与范围

三份原 native 的 SHA256 是：

| 原完成输入 | SHA256 |
|---|---|
| 同 $Z$ 原 Green | eb34e2506c1cda9c1f53b4ef44605d02034e0cddf3feef44593edd635506bb18 |
| 完整同 $Z$ cut | 8bc061ec200deb37548005297a1530d341eaa55065e70104cc5d82714aed21c5 |
| 同向 Hessian | 9360555293def4b1803da05c5c432a8f737ed4f3d62ea2b84c89e7e236ff7650 |

源核对原实际 child return code、全部门、冻结 source/worker/manifest、中心和 $Z$ 定义、原准确 $w_0$、pilot 与原物理费用身份。原 Green 对 cut 的 native 与 artifact process SHA 必须逐字吻合，仓库出版快照不能冒充 artifact process。

大 native 只由 Actions 下载并用原 lossless manifest 逐字节恢复。若本消费者数学已成功而发布失败，恢复须核原成功 child0、唯一逻辑 native 的 SHA、全部输入和门；不以旧 process.complete=false 否定已完成数学。新 summary 必须在写入前核 UTF-8 小于 60,000 bytes，全部 6391 行另保 native。

输出仍只有 finite193 压缩响应误差上界、各通道分解和独立已知 high 源。$1/200$ 若未达到就照实保存 false。未知无限 high 反馈、真正 PDE 响应、全参数 Schur 和非线性解均不由本次重权自动获得。
