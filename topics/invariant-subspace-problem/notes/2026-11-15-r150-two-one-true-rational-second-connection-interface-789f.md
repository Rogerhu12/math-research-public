# 原二点特征零第二连接：单一缺头的可续正证书入口

日期：2026-11-15 UTC。作者：Astra-ISP-789f / literature_audit。AI-assisted，GPT-6 Astra Pro。

本入口不运行新的完整原矩阵消元，不重建旧二十二个不相容大 RHS 的有理解。它从真实投影恢复全部首阶链，仅为第二阶的一个缺失首项求一列有理数校正。正结果足以证明完整 $\beta_{2,\mathbb Q}=0$；负结果只限制校正的正常次数至多三范围。

## 数学缩减

记 $C_A\to C_P$ 为同原完整输出到 pure/one-normal 输出的商映射。两者的常左核都是二十二维，投影正谱为 $1^7,2,3$，完整第一连接准确为七。因此投影的十五维 first-head 空间和完整 first-head 空间相同。投影的左 jet 延零到正常平方输出后，仍逐原来源满足完整左核方程；没有除去 $g$。

取全部真实首阶链为
$$
\lambda_0=\Lambda Hc,\qquad \lambda_1=Yc+\Lambda d,
\quad c\in\mathbb Q^{15},\ d\in\mathbb Q^{22},
$$
其中 $Y$ 只含 pure/one-normal 输出。任意同头首阶链之差都是完整常左核，所以此支持范围也适用于任意真实首阶链。

入口首先直接用原 $1088\times157$ 块 $[B_1,C]$ 恢复同一 canonical 链，$B_1=A_0^T|_{\mathrm{normal}=1}$、$C=A_1^T\Lambda$。它必须匹配旧已付 $H$、$\lambda_0$ 及完整 $605\times15$ 的 $\lambda_1$ 三个 logical SHA，并实际检查后者的 $450\times15$ 正常二次块为零。任何矛盾都停止；不以理论预期覆盖实现差异。

原第二 forcing 为
$$
R_2=A_2^T\Lambda H+A_1^TY.
$$
全部 $5100$ 个正常乘子次数至少二的来源行准确为零。小系统
$$
[B_1,C,R_2]
$$
给出投影的十四条真实第二阶链，逐 $6188$ 个来源核三层。其首项在完整十五维首头中余维一；选择一个坐标补向量 $e$，仅测试 $R_2e$。

完整 $C$ 的首连接商像是七维。若 $F$ 为 $H$ 的自由头坐标，$P$ 为另外七坐标，则原行身份
$$
C=-B_1Y E_F+C_P(I-HE_F)_P
$$
把全部二十二个首阶常校正保为七个商基，而被删除的十五项由真实 $B_1$ 像吸收。

对于 $\lambda_2$ 的正常次数至多三限制，真实高系统仅剩齐次 $H_3$。旧完整证书给其秩 $988$、核恰两维；本入口由原弱线与原切向常核恢复这两列，匹配旧全部列 SHA，并重新核全部 $10200$ 个高行乘积。其低返回列记为 $C_h$。唯一新低方程为
$$
[B_{585},C_h,C_P]\begin{pmatrix}x\\a\\b\end{pmatrix}+R_2e=0.
$$
常块为 $1088\times594$、秩 $592$。这来自旧 $[B_{585},C,C_h]$ 的准确秩 $592$ 及上述全原列空间身份。两条常齐次核来自完整常左核；保其自由规范后，已知道一组 $592$ 列基，不需重求此大块的齐次 RREF。

入口仅以预定素数十七选原行单位；若该内部选行未满秩，回退到原有理常块的转置选行。它不扫描素数，不把有限域核当有理数核。仅求这个单位块的一列实际 RHS，用已核 Dixon 例程，先存候选再核全部原单位行、完整 $1088$ 行及最终 $6188$ 原来源三层。

成功时把新链与投影十四链联合、再按真实 $15\times15$ 首项变换归一回旧首头，得到十五条完整第二阶链，故完整 $\beta_{2,\mathbb Q}=0$。最后正常平方读数保留；非零的 $\lambda_2(n_j^2)$ 还须第三阶延拓，不能立即否定 $h_0t_j$。

失败时仅说明本次 $\lambda_2$ 正常次数至多三的范围未补该头；正常四、五校正没有被宣布穷尽。完整第二连接仍只在零或一之间。

## 固定源码

主脚本：

notes/2026-11-15-r150-two-one-true-rational-second-connection-789f.py

Git blob：700a667a20237c142d2ee4d2b26213afa7dc3324

字节数：25647；SHA256：d4ff08a474ef3abe6c7ee08bea7829e6fa3d52eb2e04c71469b18b2ea2c27bb8。

依赖保旧文件字节，不改已付源码：

- 原 base：2026-11-15-r150-two-directed-original-left-two-jet-witness-789f.py，SHA 8f55c5b5f0db2a7dd9b0b042e00cd506fd6e38698b9dc264a602e3dc8ccb510b。
- 原物理 generator：2026-11-15-r150-original-transverse-first-connection-789f.py，SHA 2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186。
- 原 actions：2026-11-15-r150-original-comoving-jet-actions-through-seventeen-789f.py，SHA 2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332。
- 实际 RHS 单位 helper：2026-11-15-r150-exact-actual-rhs-unit-schur-kernel-789f.py，SHA 36356983e71ee1e67677da1a7a5f7aebf2987db282a5447a741b6a6af93084d5。

全部脚本都位于 topic 的 notes 目录。

## 小实际输入

所有路径均相对 topics/invariant-subspace-problem。

| CLI | 原小文件 | SHA256 |
|---|---|---|
| --constant-receipt | notes/2026-11-14-rank-one-physical-mean-two-rank-certificate-receipt.json | 5d83b8784ea4e1d2b99f9ccd8881dcf6f2abe4241586219a3b459541c10d6272 |
| --first-receipt | notes/r150-local-projection-session-789f/43736746064-two-directed-original-left-two-jet-resume600.json | 2a75b4dba0b1e28902bc3a441ec7ce03a7e7fbdf46abfa5c138f4f7ab29b269a |
| --full-first-receipt | notes/r150-source-kernel-session-789f/43740928483-two-full-original-first-connection-field11.json | aebdd169ec950f7eb4c17b7e9ac4dc30ecb205dfc6a2d9476af9d4d03ebc9d3a |
| --projection-receipt | notes/r150-local-projection-session-789f/43729338969-two-original-projected-order4.json | 693da6446a6f04cba2c343ea49d9d3466caad1aebd056e91db338163b20d3332 |
| --h3-receipt | notes/r150-local-projection-session-789f/43736746064-two-complete-cubic-high-field-rank.json | 92d6c57531406e5892b06632aca6a8262cd238bec926c2b73532d7e05ed3bc8e |
| --tangent-receipt | notes/r150-local-projection-session-789f/43736746064-two-tangent-coupled-cubic-first-jet-extension.json | 66c05b0911d7b003e635ca0ed43f605f1a4de32003a9da3878f1ca46b51279ab |

## 命令和续接

建议同一实际共享预算 600 秒、4 GiB，外层 660 秒。不依赖已经结束的旧 job 的大缓存。

~~~text
python MAIN.py
  --paid-probe {scripts}/2026-11-15-r150-two-directed-original-left-two-jet-witness-789f.py
  --generator {scripts}/2026-11-15-r150-original-transverse-first-connection-789f.py
  --jet-actions {scripts}/2026-11-15-r150-original-comoving-jet-actions-through-seventeen-789f.py
  --unit-schur-helper {scripts}/2026-11-15-r150-exact-actual-rhs-unit-schur-kernel-789f.py
  --constant-receipt {scripts}/2026-11-14-rank-one-physical-mean-two-rank-certificate-receipt.json
  --first-receipt {scripts}/43736746064-two-directed-original-left-two-jet-resume600.json
  --full-first-receipt {scripts}/43740928483-two-full-original-first-connection-field11.json
  --projection-receipt {scripts}/43729338969-two-original-projected-order4.json
  --h3-receipt {scripts}/43736746064-two-complete-cubic-high-field-rank.json
  --tangent-receipt {scripts}/43736746064-two-tangent-coupled-cubic-first-jet-extension.json
  --checkpoint-dir {work}/two-one-true-q-second
  --out {work}/two-one-true-q-second-receipt.json
  --remaining-seconds 600 --memory-mib 4096
~~~

每个矩阵阶段先写不可变内容地址文件，再更新 manifest；候选单位解与完整乘回状态分开。相同脚本、输入 SHA 和同一 checkpoint-dir 可恢复。receipt 只留小身份、矩阵 SHA、维数、真正原产品标志和读数；完整 cochain 仍在同一 job 临时目录供后继使用，不上传大数组。

写源后本地只尝试 AST 检查，但 exec-server 返回 os error 2，未运行任何研究数学、未重复轮询。远端执行前应按现有发布流程解析源码。以上数学数值只有旧已付输入；新增二阶结果尚未执行，不预填。
