# 动态目标数与精度的原局部完整求解封装

日期：2026-11-15。范围：有限域 \( \mathbb F_{31}[[t]]/(t^L) \)，\(t=s-2\)。本文件说明一个独立求解入口，**不记录新数学运行或新像秩结论**。

## 1. 固定数学核心与动态接口

源码：[2026-11-15-r150-saturated-local-unit-solve-789f.py](2026-11-15-r150-saturated-local-unit-solve-789f.py)。

原完整 \(G\) 仍为 \(1034\times1021\)，原 \(573\) 个常数主元先作完整 Schur 消去；随后恰为 \(461\times448\)，保留全部 \(13\) 个自由条件。所有实际列的 leading-component、原次数及原 leading coefficient 均随源输出保留。

单元 Schur 核心原样引用：

- 文件：[2026-11-14-r150-local-jet-unit-schur-helper-789f.py](2026-11-14-r150-local-jet-unit-schur-helper-789f.py)。
- SHA256：d31c917fe0aaa0e9008e5cb0a85cb81600b5a431fe691261948354fb1d1ee42b。
- 最大 Smith 指数为已付的 \(5\)，不改变该输入假设。
- 核心保存每层真实主元行列、单位逆、Schur 矩阵、右端与完整高阶回代，逐层验证完整等式。
- 本封装增加动态目标数 \(1\le NT\le229\)、使用精度 \(5<L\le20\)、缓存截取、旧五阶源锁定以及外层完整乘回。未改核心源码。

G 缓存精度可以高于本轮 RHS 精度，例如 \(G_{20}\) 用于 \(L=15\)。封装核对完整缓存的实际字节数和所有系数的规范代表，再仅使用所需系数；不把较短 RHS 当作较长 RHS。

## 2. 命令行与输出

~~~text
python 2026-11-15-r150-saturated-local-unit-solve-789f.py
  --G G-cache.bin
  --rhs rhs.bin
  --binding <64位小写十六进制流水线绑定>
  --notes-root <notes目录>
  --out <本轮输出目录>
  --remaining-seconds <同一任务真实剩余秒数>
  [--fixed-prefix-q <旧197十项完整Q文件>]
  [--checkpoint-dir <持久检查点目录>]
~~~

默认检查点目录为输出目录中的 local-solve-checkpoints。该目录可以整体复制到另一路径恢复；绑定只含代码和实际输入内容、精度、标签等语义，不含绝对路径。路径另外进入审计记录。

输出：

- complete-G-q-root2.bin：R150SQ31 格式的完整 \(1021\times NT\times L\) 源。
- local-unit-solve-receipt.json：成功时 status=completed。
- 完成 stdout 行：status=saturated-local-unit-solve-complete，并含 fullOriginalGIdentityVerified=true、all13FreeConditionsRetained=true、TaylorPrecision=L、targets=NT。
- local-solve-input-audit.json：输入哈希、完整语义绑定与当前路径。

退出码：成功 \(0\)，已保存检查点的时间边界 \(75\)，真实局部不相容 \(2\)，其他输入或恒等式错误为失败。输出二进制的外层压缩、分片及仓库持久化由总 runner 统一处理。

## 3. 输入与输出字节合同

全部整数为 little-endian；系数为 \(0,\ldots,30\) 的单字节规范代表。所有二进制长度必须准确，无忽略的尾部字节。

### \(G\) 缓存

~~~text
8 bytes: R150SG31
4*u32: 31, 1034, 1021, Lcache
64 ASCII bytes: pipeline binding
1021 records: u16 leadingComponent, u8 degree, u8 originalLC
Lcache * 1034 * 1021 coefficient bytes in [jet][row][column] order
~~~

原字典还核对 leading-component 严格递增、次数和 \(716\)、全部次数不超过 \(8\)、恰 \(573\) 个常数列；凡使用的正阶系数均核对这些常数列严格为零。完整缓存中所有 \(k>8\) 系数逐字节核对为零。随后这些高阶 G 系数共用一个零矩阵，完整乘回只做 \(k\le8\) 的非零候选乘积；仍逐一核对全部 \(L\) 个输出系数，不降低精度或改变源选择。

### RHS

~~~text
8 bytes: R150SF31
4*u32: 31, 1034, NT, L
64 ASCII bytes: pipeline binding
NT*u16: actual target labels
1034*u64: original freeKey row dictionary, retained in its original order
L * 1034 * NT coefficient bytes in [jet][row][target] order
~~~

G 与 RHS 均必须携带命令行给定的同一流水线绑定。额外封装绑定再包含实际完整输入字节 SHA256、代码 SHA256、核心 SHA256、目标标签、精度及锁定源的实际哈希。

### 完整源

~~~text
8 bytes: R150SQ31
4*u32: 31, 1021, NT, L
64 ASCII bytes: pipeline binding
NT*u16: current actual target labels
for every original G column:
    u16 leadingComponent, u8 degree, u8 originalLC
    L * NT coefficient bytes in [jet][target] order
~~~

## 4. 锁定真实旧五项的正确回代

固定前缀参数只接受旧的完整 R1503Q31、\(197\) 个目标、\(10\) 项原源文件。全部原 G 列字典必须相同，当前目标集合必须恰为这 \(197\) 个标签；可按标签重排，但不能默默截去或添加目标。旧文件的旧流水线绑定仅作审计，不要求等于新流水线绑定；**完整旧文件内容哈希进入新绑定**。

令旧源前五项为
\[
 q_{\mathrm{low}}(t)=\sum_{j=0}^{4}q_jt^j.
\]
封装先在全部 \(1034\) 行与所有 \(197\) 个目标逐系数核对
\[
 [t^j](w-Gq_{\mathrm{low}})=0,\qquad 0\le j<5.
\]
只有这些实际等式成立，才求解
\[
 Gq_{\mathrm{new}}
 =\frac{w-Gq_{\mathrm{low}}}{t^5}\pmod{t^{L-5}}.
\]
最后返回
\[
 q=q_{\mathrm{low}}+t^5q_{\mathrm{new}}\pmod{t^L}.
\]
原五项逐项核对未变，所有高项由完整回代填充。剩余精度须严格大于 Smith 上界 \(5\)，故锁定模式要求 \(L>10\)。本轮预定 \(L=20\) 符合此条件。

这不是将旧十项全部锁定，也不是只返回前五项。新求解允许改变旧第 \(5,\ldots,9\) 项；它们由原完整 \(L\) 项等式决定。

## 5. 常数主元、全部自由条件及最终乘回

设原常数列与对应主元行为 \(C,R\)，真实常数单位块为 \(A_0=G_0[R,C]\)，下块为 \(C_0\)。封装计算并验证
\[
 A_0A_0^{-1}=I_{573}.
\]
对每个系数保存
\[
 G'_k=D_k-C_0A_0^{-1}B_k,\qquad
 w'_k=V_k-C_0A_0^{-1}U_k,
\]
以及实际 \(A_0^{-1}B_k,A_0^{-1}U_k\)。这里 \(w\) 是未锁模式的原 RHS，或锁定模式正确除 \(t^5\) 后的 RHS。

核心求解 \(G'q_{\rm rest}=w'\) 后，用完整卷积
\[
 q_{\rm const}=A_0^{-1}U-(A_0^{-1}B)q_{\rm rest}
\]
回填全部 \(1021\) 个源坐标与全部使用精度。所有 \(13\) 个自由行保留至核心末层并验证全精度为零。

最后不依赖缩小系统的成功标志，而重新逐系数计算原始输入：
\[
 \sum_{i=0}^{\ell}G_iq_{\ell-i}=w_\ell,
 \qquad 0\le\ell<L,
\]
在全部 \(1034\times NT\) 个坐标核对。成功 receipt 的 allOriginalGJetCoordinatesVerified 必须为 \(1034\,NT\,L\)。

## 6. 可恢复状态与共享时钟

检查点含真实矩阵和哈希，不以状态文字代替数组：

1. 旧锁定源的逐系数低阶乘回进度。
2. 实际常数单位逆与下块；每个已完成系数的四个 Schur/回代矩阵。
3. 原核心每一层的真实行列、单位逆、Schur、右端、回代与残差。
4. 全部 \(1021\) 源每个系数矩阵及原完整乘回进度。

所有描述符路径相对检查点目录，校验存储和解压后的实际 SHA256。不同输入、代码、目标标签或精度的数组不能恢复。G 缓存高阶字节也绑定，因此不能误用另一个未验证缓存。

剩余秒数必须为正有限数；没有人为最低 \(60\) 秒门槛。计时从进入 main 开始，保留 \(\min(30,\mathrm{remaining}/4)\) 秒用于持久化。SIGTERM/SIGINT 设置停止标志，在安全检查边界退出；已完成的真实阶段可续算。检查点不把本次剩余时长纳入内容绑定，因此下一次能以新的真实剩余时长恢复。

## 7. 结论边界

本封装交付的是代码与字节合同；创建时没有运行目标数学计算。即使以后全部乘回成功，它仅证明给定原 \(G\) 在 \(s=2\) 的指定有限精度局部等式。它不证明全局多项式 \(q\) 存在，不消除其他 primary，不产生新的特征零结论，也不替代原整数 carry 与来源运输。
