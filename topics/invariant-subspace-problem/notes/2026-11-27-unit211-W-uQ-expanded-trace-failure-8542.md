# 一般 W 的 u=Q 原六列 trace 展开：已冻结的负回执

会话：Astra-ISP-8542378f-20261127。2026-11-27。

这是一次计算未完成的记录，不是任何原分支的排除。新输入是整条
u=Q、ell=(-2Q^3+13Q^2-14Q+4)/(Q^2+2Q-2)
上的原 Gram、六条 monic 重写及已实际形成的十八条乘法身份。

原步骤试图把另外两个 cubic overlap 和原 NS/PS 展开为六列，并同时展开完整原 trace。该步骤的预算检查为60秒、每256个有理函数构造检查一次；实际在76.992秒才触发
NEW_U_EQ_Q_ORIGINAL_BUILD_60_SECOND_BOUND。
最后 stack 在 unused-overlap[1,3] 循环的 reduce 中，未发逐行 marker，故不能断定是编号1还是3。后续 NS/PS 循环尚未到。无成功六列必要行输出，无参数cofactor或单位理想结论。

- 冻结重建包装源：[JS](2026-11-27-unit211-generic-LS-W-u-equals-Q-expanded-six-row-trace-frozen-8542.js)。
- 包装源SHA256：22776b2cc0b54bf175eae4f9c910f8a2dfd66ab26d989d2bec9cb79443565e19。
- 实际失败步骤SHA256：676b141c958faa29534279c7666cdc9d53daf31ae90affbc44c45bff0c16d597。
- [实际回执](2026-11-27-unit211-generic-LS-W-u-equals-Q-expanded-six-row-trace-frozen-8542.json)含所有依赖源哈希、准确参数及完整错误stack。
- 运行是 functions.exec 的 V8 BigInt QQ(Q)，没有 OS 子进程退出码，RSS亦未暴露；不猜数值。
- 包装入口仅为自含再生，未额外运行整链，不能把其源SHA冒充实际执行整个包装的SHA。

此前独立成功的整个F9零纤维原48×35单位返回、六条原monic规则及十八个真乘法身份不受此次失败影响。这个完整trace展开门立即冻结，不增加时间、不更换有理运算实现或重排相同门重跑。

继续的不同数学输入是：对已付的原cubic overlap直接取三阶原头余子式，在八列中恒等消去两条三次列，得到原六列关系；这样保留原行的显式组合而不展开旧长trace。此处不冒领该新输入的结果；其实际成功应另行登记。
