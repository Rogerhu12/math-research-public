# 新五次伴随来源：14 条独立整数多项式身份的实际返回

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

针对[新的 companion 来源说明](2026-11-28-five-bit-s2-companion-moment-source-8542.md)，在五个完全独立的 $z_i$ 上完成一次小 V8 BigInt 全展开，实际 18 毫秒，14 条身份全部通过。没有重算先前超时的 S2 费用矩阵，也没有求一次数值正性。

[独立源](2026-11-28-five-bit-s2-companion-identity-certificate-8542.mjs)与[完整小回执](2026-11-28-five-bit-s2-companion-identity-certificate-8542.json)保留全部步骤。输入为原各物理层的加权 incidence，输出核对新的 $X,X^*,F_C,H,Ce,Y,CF_{\rm mid}e,e^*e,e^*F_{\rm mid}e,F_3$，以及真正顶 Schur 与旧 R298 的完全一致。另独立核对了 $D_zJ=J\mathsf T$、$\mathbf1z^*J=J\mathsf Q$ 及前五个 Newton 矩。

全部系数是 BigInt；变量指数编码基数十六，所需总次数上界十，故无指数进位。程序末尾 Node 入口仅作可重放包装，未另称执行器已运行。

这次返回只支付新有限源表示与物理伴随的确切代数对应。它不是 S2 平方预算的证书；后者仍须由完整实际 checkpoint 和标量系数继续。
