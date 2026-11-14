# 实际 strong M20 在原共同角宽上的完整双高块重标

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

## 本次完成的对象

本次输入是 R39 的实际 q085/M20 尾输入在 rational-deep 新度规上的严格辅助参考和 canonical 盒，不是后续 q095、q105 的 stored 前缀。保留全部 46 个低参数。

明确**定义**新的强场角宽为原 q 共同连续函数 $\tau_q(r)$。不是把原 strong 包的另一个归一化角宽当成相同函数，也不是仅核对两端角宽。新 density 的 continuous_strip_origin 记录原 q 路径、SHA、原积分定义和禁止重新归一化的说明。

每胞元定义 $\sigma_n=\overline X_{s,n}/\overline X_{q,n}$，两个 $\overline X$ 都是各自包中定义的 exact dyadic。实际范围为

$$
16.33244762347011<\sigma_n<17.85329984827713.
$$

这些系数比较的是完整 canonical 包络；不声称两个实际输入向量沿同一条倍数射线。

## 严格沿用的缩放

R42 的同角宽证明对 R50 的两个真实输出支持分别适用：

$$
\Gamma^s_{\mathrm N,kn}
\le\frac{\sigma_n^2}{\sigma_k}\Gamma^q_{\mathrm N,kn},
\qquad
\Gamma^s_{\mathrm R,kn}
\le\frac{\sigma_n^2}{\sigma_k}\Gamma^q_{\mathrm R,kn}.
$$

对两个块的完整纯低源响应分别用
$\sigma_+^2/\sigma_k$；同一个独立 $Z=2^{-2200}$ 深图的 far 响应只除以 $\sigma_k$。无限源核和纯低响应用 $\sigma_+^2/\sigma_-$，无限 far 响应除以 $\sigma_-$。这些纯低界来自完整 canonical 盒和已付宽角域的通用源包络，不要求 actual strong 的 Fourier 系数等于 q 的倍数。

$V_s=\sigma_nV_q$，$A_{s,n}=\sigma_nA_{q,n}$。新 $k_s$ 向上取整到至少 $\sigma_+k_q$，从而原 $\tau_q$ 的点态导数预算仍支配新的材料预算。新接口 norm jumps、全部原 strip costs、完整 mean 小域及实际 strong 辅助 far 域均重新严格检查。

## 正式执行与结果

流式源 tail_r42_same_strip_strong_split.py 复用已准备的 strong density 构造至写盘处，只对既存两个高块逐行缩放。session 40535 正式退出 0，程序用时约 12.725 秒，完整资源记录约 12.748 秒，峰 RSS 为 50,896 KiB。

十个源/材料/角宽/接口/mean/far 门均通过。输出保留 213 个胞元、22,791 对因果位置的两份 $\Gamma$；每个导出值再向上舍入为 32 位 dyadic，新增相对放大严格小于 $2^{-31}$。

- density：tail-r42-strong-same-tau-r1-density.json.gz，281,853 bytes，SHA e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700。
- split：tail-r42-strong-same-tau-r1-split.json.gz，753,297 bytes，SHA b31ba4868bf825fe19981af820f92d798161df027519992b9380a4b9f7f6b5dd。

新 split 的 q_split_origin 明确指向完整 q 分带包。它刻意不声称新 strong 值与 q 逐位相同；原 q 的完整 identity 只作为来源事实保留。strong 数值是新的严格缩放上界。

这一步没有新的 ODE、source 积分、Node 进程或低场求解。它已提供实际 strong 的共同域及双高块输入；强低四核重标和完整 641 行联合门由后续独立账本核算。本次记录本身不宣称实际强头部已精确闭合，更不包含外部 0–11 胞元的连续径向误差或最终闭曲面标准。
