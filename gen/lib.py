import subprocess, os, tempfile, json
pages = []
def P(grp, cat, pid, title, desc, syn, time, *ex):
    pages.append(dict(grp=grp, cat=cat, id=pid, title=title, desc=desc, syntax=syn, time=time, examples=list(ex)))
def E(title, code, expl, inp="", pre=""):
    body = "".join("    " + l + "\n" if l.strip() else "\n" for l in code.strip("\n").split("\n"))
    full = "#include <bits/stdc++.h>\nusing namespace std;\n" + (pre.strip("\n") + "\n\n" if pre else "") + "int main()\n{\n" + body + "    return 0;\n}\n"
    return dict(title=title, code=full, input=inp, explain=expl, output=None)
def run_all():
    d = tempfile.mkdtemp()
    for p in pages:
        for i, e in enumerate(p["examples"]):
            src = os.path.join(d, "a.cpp"); exe = os.path.join(d, "a.out")
            open(src, "w").write(e["code"])
            c = subprocess.run(["g++", "-std=c++17", "-O1", "-o", exe, src], capture_output=True, text=True)
            if c.returncode:
                print("COMPILE FAIL", p["id"], i, c.stderr[:300]); e["output"] = "(compile error)"; continue
            r = subprocess.run([exe], input=e["input"], capture_output=True, text=True, timeout=10)
            e["output"] = r.stdout.rstrip("\n")
