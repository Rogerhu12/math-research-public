# R150：有限零点剩余三个横向泛函的完整二阶左校正入口

日期：2026-11-15 UTC。Astra-ISP-789f；AI-assisted，GPT-6 Astra Pro。

## 对象与本次边界

保持原自然参数 $s$、原十七式、全部 $6188$ 来源及 $4367$ 输出。复用已完成的零点第一横向模型与第二纯校正；本次只计算剩余三个横向左泛函的二阶延拓，不能预设完整第一连接秩恰为四。

脚本为 [2026-11-15-r150-zero-second-normal-envelope-789f.py](2026-11-15-r150-zero-second-normal-envelope-789f.py)，SHA256：
c8dde441995f3c9b57728a68ec7b29aa56e9abfbbee280fc334961b64e561403。

第一系数生成器 SHA256 为
2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186。
第一回执原字节 SHA256 为
f4926b42b03985728f684d6430d2d9c3a0dd1a03010bee0496a5a7a4e5670dbe；
有限零点第二纯回执原字节 SHA256 为
c54e5e9ce0595ddde41fcf78971a9f1d37cda36099a670579d4cd13657b5d565。
代码核对对应 chart、全部旧小矩阵哈希和完整已付身份。

## 完整来源与可用推论

以原 $K$ 而非反序矩阵生成全部到 $s^2$ 的系数，纯二阶系数为
$d^2(2400,-960,96)$，放在原 $N_8,N_9,N_{10}$，其余为零。
校正允许一次、二次横向全部 $585$ 目标；矩阵保 $170$ 纯来源和 $918$ 一次横向来源，另 $5100$ 来源按真实横向次数逐类为零。

一次 $1088\times595$ 有理 RREF 给
$[A_0^{\mathsf T}|_{\le2},A_1^{\mathsf T}Q,R]$；
旧一阶歧义后的秩只要求在 $578$ 至 $582$ 之间，不冒称它是完整第一连接的下界。若最后三列的实际增秩是 $k$，构造及全行乘回给至少 $23-k$ 个独立的完整左二阶 jet，因而
$$
r_1+r_2\le4+k,\qquad r_1\le4,\qquad
\delta_{4354,0}\ge34-k,\quad\delta_{4353,0}\ge31-k.
$$
正残差不排更高横向校正。只有实际 $k=0$ 才能更新公共零阶至至少 $34$、有限因子至 $K_{80}=s^{20}K_{60}$；即使如此，也不把它写成完整零点 $\beta_2=0$，因为 $r_1$ 尚未精确确定。

## 实际运行参数

在已有临时 session 43679903558 中排唯一 step zero-second-normal-envelope：
~~~text
--generator {scripts}/2026-11-15-r150-original-transverse-first-connection-789f.py
--first-connection-receipt {work}/original-transverse-first-connection-receipt.json
--second-pure-receipt {work}/zero-second-pure-envelope-receipt.json
--out {work}/zero-second-normal-envelope-receipt.json
--remaining-seconds 30
~~~
数学共用时钟 $30$ 秒、地址空间 $512$ MiB；外层 $80$ 秒含输入和收尾余量。这些是本步骤自选上限，不是数学停工理由。结果仅在实际回执完成后列为结论，若未完成则保具体阶段继续。

只有源码、参数、run ID、哈希和小执行记录进入仓库；完整可重算矩阵只在实际作业内临时保留，不上传大工件，不重做旧正常形或 Dixon 高位。
